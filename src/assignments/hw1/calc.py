from dataclasses import dataclass


@dataclass(frozen=True)
class Expr:
    pass


@dataclass(frozen=True)
class Num(Expr):
    value: int


@dataclass(frozen=True)
class Add(Expr):
    e1: Expr
    e2: Expr


@dataclass(frozen=True)
class Sub(Expr):
    e1: Expr
    e2: Expr


@dataclass(frozen=True)
class Mul(Expr):
    e1: Expr
    e2: Expr


@dataclass(frozen=True)
class Compose(Expr):
    e1: Expr
    e2: Expr


@dataclass(frozen=True)
class X(Expr):
    pass


def eval(x: int, e: Expr) -> int:
    match e:
        case Num(value):
            # your code here
        case Add(e1, e2):
            # your code here
        case Sub(e1, e2):
            # your code here
        case Mul(e1, e2):
            # your code here
        case Compose(e1, e2):
            # your code here
        case X():
            # your code here
