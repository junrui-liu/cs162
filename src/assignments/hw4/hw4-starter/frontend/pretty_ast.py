from PrettyPrint import PrettyPrintTree
from .lang import *
from colored import Fore, Back, Style
from typing import Optional, Any


DEFAULT_BACK = '\x1b[100m'


@dataclass
class Atom:
    s: str


ellipsis = Atom('..')


@dataclass
class LabelNode[T]:
    label: str
    content: T


@dataclass
class Result:
    value: Any
    children: list[Any]
    label: Optional[Any] = None


def style_value(fore=Fore.white, back=DEFAULT_BACK):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result: Result = func(*args, **kwargs)
            result.value = f'{fore}{back}{result.value}{DEFAULT_BACK}'
            return result
        return wrapper
    return decorator


def get(node):
    match node:
        case Atom(s):
            return Result(s, [])
        case LabelNode(l, x):
            match get(x):
                case Result(v, cs, _):
                    return Result(v, cs, l)

        case SrcMap(node, _):
            return get(node)

        case Label(l):
            return Result(l, [])

        case Binder(x, s):
            def sty(x): return f'{Fore.black}{Back.white} {x} {Style.reset}'
            vars = [sty(x.name)]
            while isinstance(s, Binder):
                vars.append(sty(s.var.name))
                s = s.scope
            return get(LabelNode('─'.join(vars), s))

        case (Label(l), t):
            return Result(l, [t])

        case Type():
            t = node
            match t:
                case TyName(name):
                    return Result(name, [])
                case TNat() | TBool():
                    return Result(wl.pformat(t), [])
                case TProd(ts):
                    if len(ts) == 0:
                        return Result('()', [])
                    else:
                        return Result('(,)', ts)
                case TFun(inp, out):
                    return Result('->', [inp, out])
                case TSum(d):
                    return Result('+', [(l, t) for l, t in d.items()])
                case _:
                    return Result(node, [])
        case Expr():
            e = node
            match e:
                case Abbrev(name):
                    return Result(name, [])
                case Nat(n):
                    return Result(wl.pformat(e), [])
                case Binop(op, e1, e2):
                    return Result(wl.pformat(op), [e1, e2])
                case Bool(b):
                    return Result(wl.pformat(e), [])
                case Ite(cond, thn, els):
                    return Result('ite', [cond, thn, els])
                case Var(name):
                    return Result(name, [])
                case Lambda(b):
                    return Result('λ', [b])
                case App(l, r):
                    return Result('$', [l, r])
                case Pack(es):
                    if len(es) == 0:
                        return Result('()', [])
                    else:
                        return Result('(,)', es)
                case Inj(Label(l), e):
                    match e:
                        case Pack([]):
                            return Result(l, [])
                        case _:
                            return Result(l, [e])
                case Let(l, r):
                    return Result('let', [l, r])
                case Match(e, bs):
                    return Result('match', ([e] + bs))
                case Annot(e, t):
                    return Result(':', [e, t])
                case _:
                    print(f'Unhandled expr: {type(e)}')
                    exit()
        case Branch(p, e):
            return Result('?', [p, e])
        case Pattern():
            return get_pattern(node)
        case _:
            return Result(node, [])


@style_value(Style.bold)
def get_pattern(p: Pattern):
    match p:
        case PWildcard():
            return Result('_', [])
        case PVar(x):
            return Result(x, [])
        case PPack(ps):
            if len(ps) == 0:
                return Result('()', [])
            else:
                return Result('(,)', ps)
        case PInj(Label(l), p):
            match p:
                case PPack([]):
                    return Result(l, [])
                case _:
                    return Result(l, [p])


def get_children(x):
    return get(x).children


def get_val(x):
    return get(x).value


def get_label(x):
    return get(x).label


pp_ast = PrettyPrintTree(get_children, get_val, get_label,
                         orientation=PrettyPrintTree.Horizontal,
                         return_instead_of_print=True)
