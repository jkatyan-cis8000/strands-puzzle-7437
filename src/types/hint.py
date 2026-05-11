from typing import NamedTuple
from enum import Enum


class HintType(Enum):
    FIRST_LETTER = "first_letter"
    REVEAL_WORD = "reveal_word"
    REMOVE_LETTERS = "remove_letters"


class Hint(NamedTuple):
    hint_type: HintType
    data: str
