from typing import List, Tuple
from src.types.board import Position, Direction

GridPosition = Tuple[int, int]


def get_neighbors(row: int, col: int, rows: int = 6, cols: int = 8) -> List[GridPosition]:
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                neighbors.append((new_row, new_col))
    return neighbors


def get_direction(start: GridPosition, end: GridPosition) -> Direction | None:
    dr = end[0] - start[0]
    dc = end[1] - start[1]
    
    if dr == 0 and dc == 0:
        return None
    
    if abs(dr) > 1 or abs(dc) > 1:
        return None
    
    if dr == -1 and dc == 0:
        return Direction.N
    elif dr == -1 and dc == 1:
        return Direction.NE
    elif dr == 0 and dc == 1:
        return Direction.E
    elif dr == 1 and dc == 1:
        return Direction.SE
    elif dr == 1 and dc == 0:
        return Direction.S
    elif dr == 1 and dc == -1:
        return Direction.SW
    elif dr == 0 and dc == -1:
        return Direction.W
    elif dr == -1 and dc == -1:
        return Direction.NW
    
    return None


def is_valid_path(path: List[GridPosition]) -> bool:
    if len(path) < 2:
        return False
    
    seen = set()
    for pos in path:
        if pos in seen:
            return False
        seen.add(pos)
        
        if not (0 <= pos[0] < 6 and 0 <= pos[1] < 8):
            return False
    
    for i in range(len(path) - 1):
        direction = get_direction(path[i], path[i + 1])
        if direction is None:
            return False
    
    return True


def path_to_word(board: Tuple[Tuple[str, ...], ...], path: List[GridPosition]) -> str:
    word = ""
    for row, col in path:
        word += board[row][col]
    return word
