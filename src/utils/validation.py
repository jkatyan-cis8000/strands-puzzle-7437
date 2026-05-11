import re
from typing import Tuple


def is_valid_word(word: str) -> bool:
    if not word:
        return False
    if len(word) < 2:
        return False
    if not re.match(r'^[A-Z]+$', word):
        return False
    return True


def is_adjacent(p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
    dr = abs(p2[0] - p1[0])
    dc = abs(p2[1] - p1[1])
    return dr <= 1 and dc <= 1 and (dr != 0 or dc != 0)


def validate_board(board: Tuple[Tuple[str, ...], ...]) -> bool:
    if not board:
        return False
    
    rows = len(board)
    if rows != 6:
        return False
    
    for row in board:
        if not isinstance(row, tuple):
            return False
        if len(row) != 8:
            return False
        for cell in row:
            if not isinstance(cell, str) or len(cell) != 1:
                return False
            if not cell.isupper():
                return False
    
    return True
