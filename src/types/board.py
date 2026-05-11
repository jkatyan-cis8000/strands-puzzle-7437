from typing import NamedTuple, Tuple
from enum import Enum


class Cell(NamedTuple):
    letter: str
    row: int
    col: int


Board = Tuple[Tuple[Cell, ...], ...]


class Position(NamedTuple):
    row: int
    col: int


class Direction(Enum):
    N = "N"
    NE = "NE"
    E = "E"
    SE = "SE"
    S = "S"
    SW = "SW"
    W = "W"
    NW = "NW"
