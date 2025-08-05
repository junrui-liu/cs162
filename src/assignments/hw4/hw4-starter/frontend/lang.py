import wadler_lindig as wl
from wadler_lindig import TextDoc as d, BreakDoc as br
from dataclasses import dataclass
from .src_loc import Src


@dataclass(frozen=True)
class SrcMap[T]:
    node: T
    src: Src

    def __repr__(self):
        return wl.pformat(self)

    def __pdoc__(self, **kwargs):
        return wl.pdoc(self.node)


@dataclass(frozen=True)
class Label:
    name: str

    def __pdoc__(self, **kwargs):
        return d(self.name)


@dataclass(frozen=True)
class Expr:

    def __repr__(self):
        return wl.pformat(self)


@dataclass(frozen=True)
class Type:

    def __repr__(self):
        return wl.pformat(self)


@dataclass(frozen=True)
class Pattern:

    def __repr__(self):
        return wl.pformat(self)


@dataclass(frozen=True)
class Abbrev(Expr):
    """Abbreviation (global variable) for expressions"""
    name: str

    def __pdoc__(self, **kwargs):
        return d(self.name)


def abbrev(name):
    return Abbrev(name)


@dataclass(frozen=True)
class Var(Expr):
    name: str

    def __pdoc__(self, **kwargs):
        return d(self.name)


def var(name):
    return Var(name)


@dataclass(frozen=True)
class Binder[T]:
    var: Var
    scope: T

    def __repr__(self):
        return wl.pformat(self)

    def __pdoc__(self, **kwargs):
        return wl.pdoc(self.var) + d(".") + br("") + wl.pdoc(self.scope)


def binder(var, scope):
    return Binder(var, scope)


@dataclass(frozen=True)
class TyName(Type):
    """Abbreviation (global variable) for types"""
    name: str

    def __pdoc__(self, **kwargs):
        return d(self.name)


def type_name(name):
    return TyName(name)


@dataclass(frozen=True)
class TNat(Type):
    def __pdoc__(self, **kwargs):
        return d("Nat")


@dataclass(frozen=True)
class TBool(Type):
    def __pdoc__(self, **kwargs):
        return d("Bool")


@dataclass(frozen=True)
class TFun(Type):
    inp: Type
    out: Type

    def __pdoc__(self, **kwargs):
        return wl.bracketed(
            d("("),
            [wl.pdoc(self.inp), wl.pdoc(self.out)],
            d(" -> ") + br(""),
            d(")"),
            kwargs["indent"])


def t_fun(inp, out):
    return TFun(inp, out)


@dataclass(frozen=True)
class TProd(Type):
    ts: list[Type]

    def __pdoc__(self, **kwargs):
        return wl.bracketed(
            d("("),
            [wl.pdoc(t) for t in self.ts],
            wl.comma,
            d(")"),
            kwargs["indent"])


def t_prod(ts):
    if len(ts) == 1:
        return ts[0]
    else:
        return TProd(ts)


@dataclass(frozen=True)
class TSum(Type):
    ts: dict[Label, Type]  # this will be a frozen dict

    def __pdoc__(self, **kwargs):
        return wl.bracketed(
            d("+{"),
            [wl.pdoc(l) + d(": ") + wl.pdoc(t) for l, t in self.ts.items()],
            wl.comma,
            d("}"),
            kwargs["indent"])


def t_sum(ts):
    return TSum(ts)


@dataclass(frozen=True)
class PWildcard(Pattern):
    def __pdoc__(self, **kwargs):
        return d("_")


def p_wildcard():
    return PWildcard()


@dataclass(frozen=True)
class PVar(Pattern):
    name: str

    def __pdoc__(self, **kwargs):
        return d(self.name)


def p_var(name):
    return PVar(name)


@dataclass(frozen=True)
class PPack(Pattern):
    ps: list[Pattern]

    def __pdoc__(self, **kwargs):
        return wl.bracketed(
            d("("),
            [wl.pdoc(p) for p in self.ps],
            wl.comma,
            d(")"),
            kwargs["indent"])


def p_pack(ps):
    if len(ps) == 1:
        return ps[0]
    else:
        return PPack(ps)


@dataclass(frozen=True)
class PInj(Pattern):
    l: Label
    p: Pattern

    def __pdoc__(self, **kwargs):
        match self.p:
            case PPack([]):
                return wl.pdoc(self.l)
            case _:
                return wl.NestDoc(
                    wl.pdoc(self.l) + br(" ") + wl.pdoc(self.p),
                    kwargs["indent"])


def p_inj(l, p):
    return PInj(l, p)


@dataclass(frozen=True)
class Nat(Expr):
    n: int

    def __pdoc__(self, **kwargs):
        return d(str(self.n))


def nat(n):
    return Nat(n)


@dataclass(frozen=True)
class NatOp:
    def __repr__(self):
        return wl.pformat(self)


@dataclass(frozen=True)
class Add(NatOp):
    def __pdoc__(self, **kwargs):
        return d("+")


@dataclass(frozen=True)
class Sub(NatOp):
    def __pdoc__(self, **kwargs):
        return d("-")


@dataclass(frozen=True)
class Mul(NatOp):
    def __pdoc__(self, **kwargs):
        return d("*")


@dataclass(frozen=True)
class Eq(NatOp):
    def __pdoc__(self, **kwargs):
        return d("==")


@dataclass(frozen=True)
class Binop(Expr):
    op: NatOp
    e1: Expr
    e2: Expr

    def __pdoc__(self, **kwargs):
        return d("(") + wl.pdoc(self.e1) + br(" ") + wl.pdoc(self.op) + d(" ") + wl.pdoc(self.e2) + d(")")


def add(e1, e2):
    return Binop(Add(), e1, e2)


def sub(e1, e2):
    return Binop(Sub(), e1, e2)


def mul(e1, e2):
    return Binop(Mul(), e1, e2)


def eq(e1, e2):
    return Binop(Eq(), e1, e2)


@dataclass(frozen=True)
class Bool(Expr):
    b: bool

    def __pdoc__(self, **kwargs):
        return d(str(self.b))


def tt():
    return Bool(True)


def ff():
    return Bool(False)


@dataclass(frozen=True)
class Ite(Expr):
    "Represent if-then-else"
    cond: Expr
    thn: Expr
    els: Expr

    def __pdoc__(self, **kwargs):
        return ((d("if ") + wl.pdoc(self.cond))
                + br(" ")
                + (d("then ") + wl.pdoc(self.thn))
                + br(" ")
                + (d("else ") + wl.pdoc(self.els))).group()


def ite(cond, thn, els):
    return Ite(cond, thn, els)


@dataclass(frozen=True)
class Lambda(Expr):
    b: Binder[Expr]

    def __pdoc__(self, **kwargs):
        return wl.NestDoc(
            d("\\") + wl.pdoc(self.b.var) + d(".") +
            br(" ") + wl.pdoc(self.b.scope),
            kwargs["indent"])


def lam(b):
    return Lambda(b)


@dataclass(frozen=True)
class App(Expr):
    l: Expr
    r: Expr

    def __pdoc__(self, **kwargs):
        return wl.NestDoc(
            d("(") + wl.pdoc(self.l) + d(")") +
            br(" ") + d("(") + wl.pdoc(self.r) + d(")"),
            kwargs["indent"])


def app(l, r):
    return App(l, r)


@dataclass(frozen=True)
class Pack(Expr):
    es: list[Expr]

    def __pdoc__(self, **kwargs):
        return wl.bracketed(
            d("("),
            [wl.pdoc(e) for e in self.es],
            wl.comma,
            d(")"),
            kwargs["indent"])


def pack(es):
    if len(es) == 1:
        return es[0]
    else:
        return Pack(es)


@dataclass(frozen=True)
class Inj(Expr):
    l: Label
    e: Expr

    def __pdoc__(self, **kwargs):
        match self.e:
            case Pack([]):
                return wl.pdoc(self.l)
            case _:
                return wl.NestDoc(
                    d("(") + wl.pdoc(self.l) + br(" ") + wl.pdoc(self.e) + d(")"),
                    kwargs["indent"])


def inj(l, e):
    return Inj(l, e)


def inj_unit(l):
    return Inj(l, Pack())


@dataclass(frozen=True)
class Branch:
    p: Pattern
    e: Expr

    def __pdoc__(self, **kwargs):
        return wl.NestDoc(
            wl.pdoc(self.p) + d(":") + br(" ") + wl.pdoc(self.e),
            kwargs["indent"])

    def __repr__(self):
        return wl.pformat(self)


def branch(p, e):
    return Branch(p, e)


@dataclass(frozen=True)
class Match(Expr):
    e: Expr
    bs: list[Branch]

    def __pdoc__(self, **kwargs):
        return d("match ") + wl.pdoc(self.e) + d(" with") + br(" ") + \
            wl.bracketed(d("{"), [wl.pdoc(b) for b in self.bs],
                         wl.comma, d("}"), indent=kwargs["indent"])


def match(e: Expr, bs: list[Branch]) -> Match:
    return Match(e, bs)


@dataclass(frozen=True)
class Let(Expr):
    e: Expr
    # this syntax means b is a Binder where type T (the type of scope) is instantiated with Ex
    b: Binder[Expr]

    def __pdoc__(self, **kwargs):
        return wl.GroupDoc(d("let ") + wl.pdoc(self.b.var) + d(" = ") + wl.pdoc(self.e) + d(" in") + br(" ") + wl.pdoc(self.b.scope))


def let(e, b):
    return Let(e, b)


@dataclass(frozen=True)
class Annot(Expr):
    e: Expr
    t: Type

    def __pdoc__(self, **kwargs):
        return wl.pdoc(self.e) + d(" : ") + br("") + wl.pdoc(self.t)


def annot(e, t):
    return Annot(e, t)


@dataclass(frozen=True)
class Def:
    t: Type
    e: Expr
    ok: bool = True


def def_(t, e, ok=True):
    return Def(t, e, ok)


@dataclass(frozen=True)
class Main:
    t: Type
    e: SrcMap[Expr]


@dataclass(frozen=True)
class Prog:
    defs: dict[Abbrev, Def]
    eqns: dict[Abbrev, Type]
    main: Main


def prog(defs, eqns, main):
    return Prog(defs, eqns, main)
