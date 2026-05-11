from typing import Dict, Set
from enum import Enum
from dataclasses import dataclass


class GameState(Enum):
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"


class WordStatus(Enum):
    FOUND = "found"
    PARTIAL = "partial"
    NOT_FOUND = "not_found"


class DiscoveryType(Enum):
    THEME_WORD = "theme_word"
    SPANGRAM = "spangram"


@dataclass
class Discovery:
    found: bool
    word_type: DiscoveryType


@dataclass
class PlayerDiscovery:
    found_words: Dict[str, Discovery]
    spangrams_found: Set[str]


@dataclass
class PuzzleSession:
    game_state: GameState
    discovered_words: PlayerDiscovery
    score: int
    hints_available: int
