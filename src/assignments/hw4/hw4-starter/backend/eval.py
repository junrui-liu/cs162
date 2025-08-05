from colored import Fore, Style
from frontend.lang import *
import frontend.pretty_ast as pretty
from .subst import subst


@dataclass
class Val:
    pass


@dataclass
class VNat(Val):
    n: int


@dataclass
class VBool(Val):
    b: bool


@dataclass
class VLambda(Val):
    b: Binder[Expr]


@dataclass
class VPack(Val):
    vs: list[Val]


@dataclass
class VInj(Val):
    l: Label
    v: Val


def val_to_expr(v: Val) -> Expr:
    match v:
        case VNat(n):
            return Nat(n)
        case VBool(b):
            return Bool(b)
        case VLambda(b):
            return Lambda(b)
        case VPack(vs):
            return Pack([val_to_expr(v) for v in vs])
        case VInj(l, v):
            return Inj(l, val_to_expr(v))
        case _:
            raise ValueError(f"Not a value: {v}")


def pp_with_conv(conv):
    def f(x):
        return pretty.pp_ast(conv(x))
    return f


pp_val_ast = pp_with_conv(val_to_expr)


class InterpreterError(Exception):
    pass


class UnknownAbbrev(InterpreterError):
    pass


class UnboundVariable(InterpreterError):
    pass


class ApplyingNonFunction(InterpreterError):
    pass


class BinopError(InterpreterError):
    pass


class IteError(InterpreterError):
    pass


class MatchError(InterpreterError):
    pass


class InvalidExpr(InterpreterError):
    pass


def match_(p: Pattern, v: Val) -> dict[Var, Val]:
    match p:
        case PWildcard():
            return {}
        case PVar(x):
            return {var(x): v}
        case PPack(ps):
            match v:
                case VPack(vs):
                    if len(ps) == len(vs):
                        sigma = {}
                        for p, v in zip(ps, vs):
                            sigma |= match_(p, v)
                        return sigma
                    else:
                        return None
                case _:
                    return None
        case PInj(l, p):
            match v:
                case VInj(j, v):
                    if l == j:
                        return match_(p, v)
                    else:
                        return None
                case _:
                    return None


def remove_srcmap(e: Expr | Binder) -> Expr | Binder:
    match e:
        case SrcMap(e):
            return remove_srcmap(e)
        case Binder(var, scope):
            return Binder(var, remove_srcmap(scope))
        case Abbrev() | Var() | Nat() | Bool():
            return e
        case Binop(o, e1, e2):
            return Binop(o, remove_srcmap(e1), remove_srcmap(e2))
        case Ite(cond, thn, els):
            return Ite(remove_srcmap(cond), remove_srcmap(thn), remove_srcmap(els))
        case Lambda(b):
            return Lambda(remove_srcmap(b))
        case App(e1, e2):
            return App(remove_srcmap(e1), remove_srcmap(e2))
        case Let(e, b):
            return Let(remove_srcmap(e), remove_srcmap(b))
        case Pack(es):
            return Pack([remove_srcmap(e) for e in es])
        case Inj(l, e):
            return Inj(l, remove_srcmap(e))
        case Match(e, bs):
            return Match(remove_srcmap(e), [Branch(b.p, remove_srcmap(b.e)) for b in bs])
        case Annot(e, t):
            return Annot(remove_srcmap(e), t)
        case _:
            raise InvalidExpr(e)


def traced(f):
    indent = 0

    def eval(self, e):
        nonlocal indent
        print(
            f"{' ' * indent}{Fore.red}{Style.bold}eval{Style.reset} {wl.pformat(e)}")
        # print(type(e))
        indent += 1
        v = f(self, e)
        indent -= 1
        print(
            f"{' ' * indent}{Fore.green}{Style.bold}eval{Style.reset} {wl.pformat(e)} {Fore.green}{Style.bold}=>{Style.reset} {wl.pformat(val_to_expr(v))}")
        return v
    return eval


@dataclass
class Interpreter:
    prog: Prog

    def run(self):
        return self.eval(remove_srcmap(self.prog.main.e))

    @traced
    def eval(self, e: Expr) -> Val:
        match e:

            case Abbrev(x):
                if e in self.prog.defs:
                    return self.eval(remove_srcmap(self.prog.defs[e].e))
                else:
                    raise UnknownAbbrev(x)

            case Nat(n):
                return VNat(n)

            case Binop(op, e1, e2):
                match self.eval(e1), self.eval(e2):
                    case VNat(n1), VNat(n2):
                        match op:
                            case Add():
                                return VNat(n1 + n2)
                            case Mul():
                                return VNat(n1 * n2)
                            case Sub():
                                n = n1 - n2
                                if n < 0:
                                    return VNat(0)
                                else:
                                    return VNat(n)
                            case Eq():
                                return VBool(n1 == n2)
                    case v, VNat():
                        raise BinopError(v)
                    case VNat(), v:
                        raise BinopError(v)
                    case v1, _:
                        raise BinopError(v1)

            case Bool(n):
                return VBool(n)

            case Ite(cond, thn, els):
                match self.eval(cond):
                    case VBool(True):
                        return self.eval(thn)
                    case VBool(False):
                        return self.eval(els)
                    case v:
                        raise IteError(v)

            case Var(x):
                raise UnboundVariable(x)

            case Lambda(b):
                return VLambda(b)

            case App(e1, e2):
                match self.eval(e1):
                    case VLambda(b):
                        v = self.eval(e2)
                        body = subst({b.var: val_to_expr(v)}, b.scope)
                        return self.eval(body)
                    case v:
                        raise ApplyingNonFunction(v)

            case Let(e, b):
                v = self.eval(e)
                body = subst({b.var: val_to_expr(v)}, b.scope)
                return self.eval(body)

            case Pack(es):
                return VPack([self.eval(e) for e in es])

            case Inj(l, e):
                return VInj(l, self.eval(e))

            case Match(scrut, bs):
                v = self.eval(scrut)
                for b in bs:
                    d = match_(b.p, v)
                    if d is not None:
                        e1 = subst({x: val_to_expr(v)
                                   for x, v in d.items()}, b.e)
                        return self.eval(e1)
                raise MatchError(
                    f"No match for {wl.pformat(v)} in {wl.pformat(e)}")

            case Annot(e, _):
                return self.eval(e)

            case _:
                raise InvalidExpr(e)


if __name__ == '__main__':
    import frontend.parse as parse
    program = parse.parse_stdin()
    e = Interpreter(program)
    print(f"Result: {wl.pformat(val_to_expr(e.run()))}")
