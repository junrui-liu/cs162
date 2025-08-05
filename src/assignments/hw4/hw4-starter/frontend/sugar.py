from .lang import *


def desugar_switch(cond: Expr, cases: list[tuple[Label, str, Expr]]) -> Match:
    return Match(
        cond,
        [Branch(PInj(l, PVar(x)), e) for (l, x, e) in cases]
    )


def desugar_unpack(e: Expr, xs: list[str], scope: Expr) -> Match:
    return Match(
        e,
        [Branch(PPack([PVar(x) for x in xs]), scope)]
    )
