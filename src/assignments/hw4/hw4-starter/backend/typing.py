import itertools
from dataclasses import field
from typing import Any
import wadler_lindig as wl
from wadler_lindig import pformat as pf, pdoc as pd, pprint as pp
from colored import Fore, Style
from frontend.lang import *


# typing environment (aka Gamma) that maps variables to types
type Env = dict[Var, Type]


###############################################################################
#     Auxiliary classes and functions (you don't need to understand these)    #
###############################################################################
@dataclass
class Event:
    pass


@dataclass
class ECheck(Event):
    env: Env
    e: Expr
    t: Type

    def __str__(self):
        return wl.pformat((d(f"{Fore.cyan}[check]{Style.reset}") + br(" ") +
                          wl.pdoc(self.e) + br(" ") + d(f"{Fore.cyan}:{Style.reset}") + br(" ") +
                          d(f"{Style.underline}") + wl.pdoc(self.t) + d(f"{Style.reset}")).group())


@dataclass
class ESynth(Event):
    env: Env
    e: Expr

    def __str__(self):
        return f"{Fore.green}[synth]{Style.reset} {pf(self.e)}"


@dataclass
class EContext(Event):
    src: Src

    def __str__(self):
        return f"<context>"


@dataclass
class EMatch(Event):
    p: Pattern
    t: Type

    def __str__(self):
        return f"{Fore.yellow}[match]{Style.reset} {pf(self.p)} {Fore.yellow}:{Style.reset} {Style.underline}{pf(self.t)}{Style.reset}"


def is_context(event: Event) -> bool:
    match event:
        case EContext():
            return True
        case _:
            return False


@dataclass
class Trace:
    events: list[Event] = field(default_factory=list)
    ns: list[int] = field(default_factory=list)
    indent: int = 0

    def push(self, event: Event):
        if not is_context(event):
            print(
                f"{'\n'.join([' ' * self.indent + l for l in str(event).split('\n')])}")
        self.events.append(event)
        self.ns.append(1)
        self.indent += 1

    def push_context(self, node: Any) -> Any:
        n = 0
        while True:
            match node:
                case SrcMap(node1, src):
                    self.events.append(EContext(src))
                    node = node1
                    n += 1
                case _:
                    break
        self.ns.append(n)
        return node

    def pop(self):
        n = self.ns.pop()
        for _ in range(n):
            e = self.events.pop()
            if not is_context(e):
                self.indent -= 1


trace: Trace = Trace()


class TypeError(Exception):
    pass


class MatchError(TypeError):
    pass


###############################################################################
#      Type-checking classes and functions (you need to implement these)      #
###############################################################################

@dataclass
class Checker:
    prog: Prog
    e: Expr
    t: Type

    def match_(self, p: Pattern, t: Type):
        env: Env = {}

        def trace_match(match_):
            def f(p, t):
                p = trace.push_context(p)
                trace.push(EMatch(p, t))
                result = match_(p, t)
                trace.pop()
                trace.pop()
                return result
            return f

        @trace_match
        def helper(p: Pattern, t: Type) -> Env:
            """Attmpt to match type t with pattern p
            If the match is successful, the env is modified to map pattern variables to types
            Otherwise, a MatchError is raised"""
            pass
            # your code here

        helper(p, t)
        return env

    def trace_check(check):
        def f(self, env, e, t):
            e = trace.push_context(e)
            trace.push(ECheck(env, e, t))
            t = check(self, env, e, t)
            trace.pop()
            trace.pop()
            return t
        return f

    @trace_check
    def check(self, env: Env, e: Expr, t: Type):

        match e:

            case Lambda(b):
                pass
                # your code here

            case Pack(es):
                pass
                # your code here

            case Inj(l, e):
                pass
                # your code here

            # more cases here

            case _:
                # this is the rule where up meets down
                t1 = self.synth(env, e)
                if t1 != t:
                    raise TypeError(
                        f"I expect {wl.pformat(e)} to have type {wl.pformat(t)}, but I synthesized {wl.pformat(t1)} instead")

    def trace_synth(synth):
        def f(self, env, e):
            e = trace.push_context(e)
            trace.push(ESynth(env, e))
            t = synth(self, env, e)
            trace.pop()
            trace.pop()
            print(
                f"{' '*trace.indent}{Style.bold}{Fore.green}[synth]{Style.reset} {pf(e)} {Fore.green}:{Style.reset} {Style.underline}{pf(t)}{Style.reset}")
            return t
        return f

    @trace_synth
    def synth(self, env: Env, e: Expr) -> Type:
        match e:
            case Nat():
                return TNat()

            case Bool():
                return TBool()

            case Binop(op, e1, e2):
                pass
                # your code here

            case Abbrev():
                if e in self.prog.defs:
                    return self.prog.defs[e].t
                else:
                    raise TypeError(f"Unknown abbreviation {x}")

            case Var(x):
                pass
                # your code here

            # more cases here

            case _:
                raise TypeError(
                    f"Synthesis is unavailable for this expression")

    def run(self):
        self.check({}, self.e, self.t)


def run(prog: Prog):
    checker = Checker(prog, prog.main.e, prog.main.t)
    for id, d in prog.defs.items():
        print(
            f"\n{Style.bold}Type-checking definition {wl.pformat(id)}{Style.reset}")
        checker = Checker(prog, d.e, d.t)
        if d.ok:
            checker.run()
        else:
            try:
                checker.run()
                raise TypeError(
                    f"I expect {id.name} to be ill-typed, but checking succeeded")
            except:
                pass
    checker = Checker(prog, prog.main.e, prog.main.t)
    checker.run()


if __name__ == '__main__':

    import frontend.parse as parse
    program = parse.parse_stdin()
    try:
        run(program)
    except TypeError as e:
        src = None
        for ev in trace.events:
            match ev:
                case EContext(src):
                    src = src
        print(f"Type error: {e}")

        print("when I'm doing this: {}.\n".format(
            list(itertools.dropwhile(is_context, reversed(trace.events)))[0]))
        if src is not None:
            span = 40
            start = src.start_pos
            end = src.end_pos
            before = parse._input[start-span:start].rsplit('\n', 1)[-1]
            ctx = parse._input[start:end]
            after = parse._input[end:end+span].split('\n', 1)[0]
            print(
                f"This occured at line {src.start_row}:{src.start_col} - line {src.end_row}:{src.end_col}:\n")
            lines = (before + ctx + after).split('\n')
            print(lines[0])
            for l in lines[1:]:
                print(l)
            print(' ' * len(before.expandtabs()) +
                  f'{Fore.red}{Style.bold}^{Style.reset}')
