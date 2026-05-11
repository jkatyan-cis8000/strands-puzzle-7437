from src.providers.scoring import calculate_word_score
from src.providers.hints import check_hint_unlock


def process_command(command: str, session, words: set, spangrams: set) -> None:
    """Process player command and update session state."""
    from src.types.word import WordType
    from src.types.game import Discovery, DiscoveryType
    
    if command in words:
        if command not in session.discovered_words.found_words:
            session.discovered_words.found_words[command] = Discovery(
                found=True,
                word_type=DiscoveryType.THEME_WORD
            )
            session.score += calculate_word_score(command, WordType.THEME_WORD)
    elif command in spangrams:
        if command not in session.discovered_words.spangrams_found:
            session.discovered_words.spangrams_found.add(command)
            session.score += calculate_word_score(command, WordType.SPANGRAM)
