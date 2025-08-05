import sys
import wadler_lindig as wl
import logging
import lark as lark
from lark import Lark, Transformer, v_args
from . import lang
from .src_loc import Src
from .pretty_ast import pp_ast
from .sugar import desugar_unpack, desugar_switch


_input = None


def meta_to_src(meta):
    """Convert a lark meta object to a source location"""
    return Src(meta.line, meta.column, meta.end_line,
               meta.end_column, meta.start_pos, meta.end_pos)


def src_map[T](node: T, meta) -> lang.SrcMap[T]:
    """Augment a node with source location"""
    return lang.SrcMap(node, meta_to_src(meta))


def map_src(func):
    """Post-compose a function with source mapping"""

    def f(self, meta, items):
        node = func(self, meta, items)
        return src_map(node, meta)
    return f


# def map_src(func):
#     def f(self, meta, items):
#         return func(self, meta, items)
#     return f


@v_args(meta=True)
class AstTransformer(Transformer):

    # Terminals

    def LOCAL(self, t):
        return t.value

    def GLOBAL(self, t):
        return t.value

    def LABEL(self, t):
        return lang.Label(t.value)

    # Non-terminals

    def prog(self, meta, items):
        *decls, main = items
        eqns, defs = {}, {}
        for (sort, k, v) in decls:
            match sort:
                case "eqn":
                    eqns[k] = v
                case "def":
                    defs[k] = v
                case _:
                    raise

        return lang.Prog(defs, eqns, main)

    def eqn(self, meta, items):
        name, t = items
        return ("eqn", lang.type_name(name), t)

    def def_(self, meta, items):
        name, t, e = items
        d = lang.def_(t, e)
        return ("def", lang.abbrev(name), d)

    def fail(self, meta, items):
        name, params, t, e = items
        d = lang.def_(t, e, ok=False)
        return ("def", name, d)

    def main(self, meta, items):
        t, e = items
        return lang.Main(t, e)

    def ty_nat(self, meta, items):
        return lang.TNat()

    def ty_bool(self, meta, items):
        return lang.TBool()

    def ty_name(self, meta, items):
        name, *args = items
        return lang.type_name(name)

    def ty_prod(self, meta, items):
        return lang.t_prod(list(items))

    def ty_fun(self, meta, t1_t2):
        return lang.t_fun(*t1_t2)

    def ty_field(self, meta, l_t):
        l, t = l_t
        return (l, t)

    def ty_sum(self, meta, items):
        return lang.t_sum(dict(items))

    @map_src
    def perform(self, meta, eff_arg):
        return lang.perform(*eff_arg)

    @map_src
    def lam(self, meta, items):
        var, body = items
        return lang.lam(lang.binder(lang.var(var), body))

    @map_src
    def lam_match(self, meta, branches):
        x = lang.var("_arg")
        return lang.lam(lang.binder(x, lang.match(x, branches)))

    @map_src
    def let(self, meta, items):
        x, t, e1, e2 = items
        if t is None:
            return lang.let(e1, lang.binder(lang.var(x), e2))
        else:
            return lang.let(lang.annot(e1, t), lang.binder(lang.var(x), e2))

    @map_src
    def annot(self, meta, items):
        return lang.annot(*items)

    @map_src
    def app(self, meta, items):
        return lang.app(*items)

    @map_src
    def inj(self, meta, items):
        return lang.inj(*items)

    @map_src
    def inj_unit(self, meta, items):
        (l,) = items
        return lang.inj(l, lang.pack([]))

    @map_src
    def var(self, meta, x):
        return lang.var(*x)

    @map_src
    def abbrev(self, meta, x):
        return lang.abbrev(*x)

    @map_src
    def nat(self, meta, items):
        (n_str, ) = items
        return lang.nat(int(n_str))

    @map_src
    def add(self, meta, items):
        e1, e2 = items
        return lang.add(e1, e2)

    @map_src
    def sub(self, meta, items):
        e1, e2 = items
        return lang.sub(e1, e2)

    @map_src
    def mul(self, meta, items):
        e1, e2 = items
        return lang.mul(e1, e2)

    @map_src
    def eq(self, meta, items):
        e1, e2 = items
        return lang.eq(e1, e2)

    @map_src
    def true(self, meta, items):
        return lang.tt()

    @map_src
    def false(self, meta, items):
        return lang.ff()

    @map_src
    def ite(self, meta, items):
        cond, thn, els = items
        return lang.ite(cond, thn, els)

    @map_src
    def pack(self, meta, items):
        return lang.pack(list(items))

    @map_src
    def unpack(self, meta, items):
        *xs, e1, e2 = items
        return desugar_unpack(e1, xs, e2)

    @map_src
    def switch(self, meta, items):
        scrutinee, *cases = items
        return desugar_switch(scrutinee, cases)

    def case_(self, meta, items):
        label, var, expr = items
        return (label, var, expr)

    @map_src
    def match_(self, meta, items):
        scrutinee, *branches = items
        return lang.match(scrutinee, branches)

    def branch(self, meta, items):
        pat, e = items
        return lang.branch(pat, e)

    def pat_local(self, meta, items):
        (x,) = items
        if x == "_":
            return lang.p_wildcard()
        else:
            return lang.p_var(x)

    def pat_inj(self, meta, items):
        return lang.p_inj(*items)

    def pat_inj_unit(self, meta, items):
        (l,) = items
        return lang.p_inj(l, lang.p_pack([]))

    def pat_pack(self, meta, items):
        return lang.p_pack(list(items))


def handle_errors(e):
    print("I ran into a problem during parsing...\n")
    match e:
        # UnexpectedCharacters is a lexer error, which keeps a copy of input
        # and prints the context by default
        case lark.UnexpectedCharacters():
            pass
        # parser errors don't have a copy of input, so if we want an error context,
        # we have to explicitly construct using the cached input
        case _:
            print(e.get_context(_input))
    print(e)
    # exit()
    return False


parser = Lark.open("grammar.lark", rel_to=__file__,
                   parser='lalr', propagate_positions=True)
transformer = AstTransformer()


def parse_tree(s):
    global _input
    _input = s
    print(s)
    return parser.parse(s, on_error=handle_errors)


def parse(s):
    return transformer.transform(parse_tree(s))


def parse_stdin():
    return parse(sys.stdin.read())


def parse_string(s):
    return parse(s)


def parse_file(path):
    s = None
    with open(path) as f:
        s = f.read()
    if s is not None:
        return parse(s)
    else:
        raise


if __name__ == '__main__':
    pt = parse_tree(sys.stdin.read())
    pt.pretty()
    prog = transformer.transform(pt)
    for (x, d) in prog.defs.items():
        print(x)
        print(f"type: {wl.pformat(d.t)}")
        print(pp_ast(d.e))
        print(wl.pformat(d.e))
    print("main")
