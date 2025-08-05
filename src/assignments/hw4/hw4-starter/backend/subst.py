from typing import Any
from frontend.lang import *


def subst(sigma: dict[Var, Any], node: SrcMap | Expr | Binder):
    if len(sigma) == 0:
        return node
    match node:
        case SrcMap(node, src):
            return SrcMap(subst(sigma, node), src)
        case Binder(var, scope):
            pass
            # your code here
        case Expr():
            e = node
            match e:
                case Nat() | Bool():
                    pass
                    # your code here
                case Binop(op, e1, e2):
                    pass
                    # your code here
                case Ite(cond, thn, els):
                    pass
                    # your code here
                case Abbrev():
                    return e
                case Var(_):
                    pass
                    # your code here
                case Lambda(b):
                    pass
                    # your code here
                case App(e1, e2):
                    pass
                    # your code here
                case Let(e, b):
                    pass
                    # your code here
                case Pack(es):
                    pass
                    # your code here
                case Inj(l, e):
                    pass
                    # your code here
                case Match(e, bs):
                    return Match(
                        subst(sigma, e),
                        [subst_branch(sigma, b) for b in bs])
                case Annot(e, t):
                    pass
                    # your code here


def free_vars_pat(p: Pattern) -> set[Var]:
    """Return the set of free variables in a pattern."""
    pass
    # your code here


def subst_branch(sigma: dict[Var, Any], b: Branch) -> Branch:
    pass
    # your code here
