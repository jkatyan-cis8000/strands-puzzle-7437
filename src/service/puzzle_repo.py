from typing import List, Dict, Any

from src.repo.puzzle_repo import load_puzzles, save_puzzles, PuzzleData


def get_all_puzzles(filepath: str = None) -> List[PuzzleData]:
    """Get all puzzles from repo."""
    return load_puzzles(filepath)


def get_puzzle_by_id(puzzle_id: str, filepath: str = None) -> PuzzleData:
    """Get specific puzzle from repo."""
    return load_puzzles(filepath)


def save_puzzle_data(puzzles: List[PuzzleData], filepath: str = None) -> None:
    """Save puzzles to repo."""
    save_puzzles(puzzles, filepath)
