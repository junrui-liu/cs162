
from dataclasses import dataclass
from abc import ABC
from .src_loc import Src


class Diagnostic(ABC):
    pass


class DiagnosticWithSrc(Diagnostic):
    def __init__(self, loc: Src):
        self.loc = loc


class LexerError(DiagnosticWithSrc):
    def __init__(self, char, loc: Src):
        super().__init__(loc)
        self.char = char


class Reporter:
    def __init__(self):
        pass

    def diagnose(self, d: Diagnostic):
        match d:
            case DiagnosticWithSrc():
                print("In")
                for i in range(d.loc.start_row, d.loc.end_row+1):
                    print(" {:>3}".format(""))
                    print(" {:>3} | {}".format(i+1, d.loc.lines[i]))
                    print(" {:>3}   {}".format("", " " * d.loc.start_col +
                          "^" * (d.loc.end_col - d.loc.start_col)))
                match d:
                    case LexerError():
                        print("I found illegal character '{}'".format(d.char))
            case _:
                print("I don't know how to handle this diagnostic: {}".format(d))
        # exit()


reporter = Reporter()
