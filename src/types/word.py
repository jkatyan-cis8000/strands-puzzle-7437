from typing import List, NamedTuple, Tuple
from enum import Enum
from .board import Position


class Path(NamedTuple):
    positions: List[Position]


class WordType(Enum):
    THEME_WORD = "theme_word"
    SPANGRAM = "spangram"
    NON_THEME = "non_theme"


class WordCandidate(NamedTuple):
    word: str
    path: Path
    word_type: WordType
