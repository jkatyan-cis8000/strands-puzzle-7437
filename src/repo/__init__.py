# Repo layer
# Data access - file-based persistence

from .puzzle_repo import load_puzzles, save_puzzles, load_puzzle_by_id
from .session_repo import save_session, load_session

__all__ = [
    "load_puzzles",
    "save_puzzles",
    "load_puzzle_by_id",
    "save_session",
    "load_session",
]
