# Utils Layer Design

## Overview

The utils layer provides pure helper functions for grid operations and validation.

## Files

### grid.py

Contains pure helper functions for grid operations:

- **get_neighbors(row, col, rows=6, cols=8)**: Returns list of valid neighboring positions
  - Checks all 8 directions (including diagonals)
  - Respects grid boundaries
  
- **get_direction(start, end)**: Returns Direction enum or None
  - Only returns direction for adjacent positions
  - Returns None for same position or non-adjacent positions
  
- **is_valid_path(path)**: Validates a path through the grid
  - Checks path has at least 2 positions
  - Ensures no position is visited twice
  - Verifies all positions are within grid bounds
  - Confirms consecutive positions are adjacent
  
- **path_to_word(board, path)**: Extracts word from path
  - Reads letters from board at each position in path
  - Returns concatenated string

### validation.py

Contains pure validation functions:

- **is_valid_word(word)**: Validates word format
  - Checks word is non-empty
  - Minimum length of 2 characters
  - Only uppercase letters allowed
  
- **is_adjacent(p1, p2)**: Checks if two positions are adjacent
  - Considers all 8 directions (including diagonals)
  - Positions must be different
  
- **validate_board(board)**: Validates board structure
  - Checks board has exactly 6 rows
  - Each row has exactly 8 columns
  - Each cell is a single uppercase letter

## Design Decisions

1. **Pure functions**: All functions are side-effect free and use only built-in types or types from src.types

2. **Default parameters**: get_neighbors uses default grid dimensions (6x8) matching settings

3. **Type consistency**: Uses GridPosition = Tuple[int, int] for function signatures while importing Direction from src.types

4. **Validation scope**: Functions validate specific aspects (word format vs. board structure) for reusability

## Usage

```python
from src.utils import grid, validation

# Get valid neighbors
neighbors = grid.get_neighbors(2, 3)

# Validate a path
is_valid = grid.is_valid_path([(0, 0), (0, 1), (0, 2)])

# Extract word from path
word = grid.path_to_word(board, path)

# Validate word
if validation.is_valid_word("APPLE"):
    # Process valid word

# Validate board structure
if validation.validate_board(board):
    # Board is valid
```
