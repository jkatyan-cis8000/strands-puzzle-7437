from src.repo.puzzle_repo import load_puzzle as _load_puzzle
from src.utils.grid import generate_grid


def load_puzzle() -> dict:
    """Load puzzle data from repo layer."""
    return _load_puzzle()


def generate_board(words: list, spangrams: list) -> list:
    """Generate board grid using utils."""
    all_words = words + spangrams
    return generate_grid(all_words)
