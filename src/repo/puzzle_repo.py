import json
import os
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

from src.types.game import PuzzleSession


@dataclass
class PuzzleData:
    id: str
    theme: str
    words: List[str]
    spangram: str


def load_puzzles(filepath: str) -> List[PuzzleData]:
    with open(filepath, 'r') as f:
        data = json.load(f)
    return [
        PuzzleData(
            id=puzzle['id'],
            theme=puzzle['theme'],
            words=puzzle['words'],
            spangram=puzzle['spangram']
        )
        for puzzle in data
    ]


def save_puzzles(puzzles: List[PuzzleData], filepath: str) -> None:
    data = [
        {
            'id': p.id,
            'theme': p.theme,
            'words': p.words,
            'spangram': p.spangram
        }
        for p in puzzles
    ]
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def load_puzzle_by_id(puzzle_id: str, filepath: str) -> Optional[PuzzleData]:
    puzzles = load_puzzles(filepath)
    for puzzle in puzzles:
        if puzzle.id == puzzle_id:
            return puzzle
    return None


def load_puzzle(filepath: str = None) -> Dict[str, Any]:
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), '..', '..', settings.DEFAULT_PUZZLES_FILE)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Puzzle file not found: {filepath}")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        puzzle = data[0]
    else:
        puzzle = data
    
    spangrams = puzzle.get('spangrams', [puzzle.get('spangram')]) if 'spangram' in puzzle else []
    
    return {
        'theme': puzzle['theme'],
        'words': puzzle['words'],
        'spangrams': spangrams,
        'board': _generate_board(puzzle)
    }


def _generate_board(puzzle: Dict[str, Any]) -> List[List[str]]:
    from src.utils.grid import generate_grid
    words = puzzle['words']
    spangrams = [puzzle.get('spangram')] if 'spangram' in puzzle else puzzle.get('spangrams', [])
    all_words = words + spangrams
    return generate_grid(all_words)
