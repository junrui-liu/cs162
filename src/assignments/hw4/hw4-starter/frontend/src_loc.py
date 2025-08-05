from dataclasses import dataclass


@dataclass
class Src:
    start_row: int
    start_col: int
    end_row: int
    end_col: int
    start_pos: int
    end_pos: int
