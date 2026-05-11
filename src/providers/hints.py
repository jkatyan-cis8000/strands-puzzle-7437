from typing import NamedTuple, Tuple
from src.types.game import PuzzleSession, DiscoveryType
from src.config.settings import HINT_THRESHOLD


class Hint(NamedTuple):
    content: str
    word_type: str
    word: str


def check_hint_unlock(session: PuzzleSession) -> Tuple[bool, Hint]:
    non_theme_words = [
        word for word, discovery in session.discovered_words.found_words.items()
        if discovery.word_type == DiscoveryType.THEME_WORD
    ]
    
    words_without_spangrams = [
        word for word in non_theme_words
        if word not in session.discovered_words.spangrams_found
    ]
    
    non_theme_count = len(words_without_spangrams)
    
    if non_theme_count > 0 and non_theme_count % HINT_THRESHOLD == 0:
        hint = get_next_hint(session)
        return (True, hint)
    
    return (False, Hint(content="", word_type="", word=""))


def get_next_hint(session: PuzzleSession) -> Hint:
    non_theme_words = [
        word for word, discovery in session.discovered_words.found_words.items()
        if discovery.word_type == DiscoveryType.THEME_WORD
    ]
    
    if not non_theme_words:
        return Hint(content="", word_type="", word="")
    
    latest_word = non_theme_words[-1]
    return Hint(
        content=f"Look for words related to: {latest_word}",
        word_type="non_theme",
        word=latest_word
    )
