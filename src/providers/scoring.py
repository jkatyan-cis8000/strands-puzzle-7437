from typing import List, Dict
from src.types.word import WordType
from src.types.game import PlayerDiscovery


def calculate_word_score(word: str, word_type: WordType) -> int:
    base_score = len(word)
    multiplier = _get_type_multiplier(word_type)
    return base_score * multiplier


def calculate_session_score(session) -> int:
    discovered = session.discovered_words
    score = 0
    
    for word, discovery in discovered.found_words.items():
        word_type = _discovery_type_to_word_type(discovery.word_type)
        score += calculate_word_score(word, word_type)
    
    for spangram in discovered.spangrams_found:
        score += calculate_word_score(spangram, WordType.SPANGRAM)
    
    return score


def _get_type_multiplier(word_type: WordType) -> int:
    multipliers = {
        WordType.THEME_WORD: 1,
        WordType.SPANGRAM: 2,
        WordType.NON_THEME: 1,
    }
    return multipliers.get(word_type, 1)


def _discovery_type_to_word_type(discovery_type) -> WordType:
    mapping = {
        "theme_word": WordType.THEME_WORD,
        "spangram": WordType.SPANGRAM,
    }
    return mapping.get(discovery_type, WordType.NON_THEME)
