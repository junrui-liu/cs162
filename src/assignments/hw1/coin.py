from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Program:
    pass


@dataclass(frozen=True)
class Pass(Program):
    pass


@dataclass(frozen=True)
class Print(Program):
    msg: str


@dataclass(frozen=True)
class Seq(Program):
    s1: Program
    s2: Program


@dataclass(frozen=True)
class Raise(Program):
    pass


@dataclass(frozen=True)
class If(Program):
    s1: Program
    s2: Program


@dataclass(frozen=True)
class While(Program):
    s: Program


@dataclass
class Coin:
    def flip(self) -> bool:
        import random
        return random.choice([True, False])


@dataclass
class ProbablisticInterpreter:
    coin: Coin

    def run(self, p: Program) -> Optional[str]:
        match p:
            case Pass():
                return ""
            case Raise():
                return None
            case Print(msg=msg):
                return msg
            case Seq(s1, s2):
                # your code here
            case If(s1, s2):
                # your code here
            case While(s):
                # your code here
