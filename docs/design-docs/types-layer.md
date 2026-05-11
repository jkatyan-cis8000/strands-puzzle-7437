# Types Layer Design

This document describes the type definitions for the Strands puzzle game domain model.

## Overview

The types layer defines all data structures used throughout the application. These are pure type definitions with no business logic—logic is implemented in separate layers (utils, service, etc.).

## Module Structure

```
src/types/
├── __init__.py   # Exports all types
├── board.py      # Board and cell types
├── game.py       # Game state types
├── word.py       # Word discovery types
└── hint.py       # Hint system types
```

## Type Definitions

### board.py

**Cell**
- A named tuple representing a single cell on the board
- Fields: `letter` (str), `row` (int), `col` (int)

**Board**
- Type alias for a 2D grid: `Tuple[Tuple[Cell, ...], ...]`
- Represents a 6-row × 8-column grid of cells

**Position**
- A named tuple representing coordinates: `(row: int, col: int)`
- Used for movement and location tracking

**Direction**
- Enum for 8 cardinal directions:
  - N, NE, E, SE, S, SW, W, NW
- Used for determining word formation paths

### game.py

**GameState**
- Enum representing the current game status:
  - `PLAYING`: Active game
  - `WON`: Player has found all words
  - `LOST`: Game over

**WordStatus**
- Enum representing a word's discovery status:
  - `FOUND`: Word has been correctly identified
  - `PARTIAL`: Word is incomplete
  - `NOT_FOUND`: Word not yet discovered

**DiscoveryType**
- Enum for word classification:
  - `THEME_WORD`: Word matching the day's theme
  - `SPANGRAM`: Special word that spans theme words

**Discovery**
- Tracks whether a word was found and its type
- Fields: `found` (bool), `word_type` (DiscoveryType)

**PlayerDiscovery**
- Tracks all player discoveries
- Fields: `found_words` (Dict[str, Discovery]), `spangrams_found` (Set[str])

**PuzzleSession**
- Complete game state for a session
- Fields: `game_state`, `discovered_words`, `score`, `hints_available`

### word.py

**Path**
- Named tuple representing a word's path through the grid
- Fields: `positions` (List[Position])

**WordType**
- Enum for word classification:
  - `THEME_WORD`: Matches theme
  - `SPANGRAM`: Spans theme words
  - `NON_THEME`: Random word not in theme

**WordCandidate**
- Represents a discovered word candidate
- Fields: `word` (str), `path` (Path), `word_type` (WordType)

### hint.py

**HintType**
- Enum for hint types:
  - `FIRST_LETTER`: Reveal first letter
  - `REVEAL_WORD`: Reveal entire word
  - `REMOVE_LETTERS`: Remove incorrect letters

**Hint**
- Named tuple for hint data
- Fields: `hint_type` (HintType), `data` (str)

## Design Decisions

1. **NamedTuple vs dataclass**: Used NamedTuple for immutable, simple types (Cell, Position, Path, WordCandidate) and dataclass for more complex state containers (PuzzleSession, PlayerDiscovery)

2. **Type imports**: word.py imports from board.py for Position type—this creates a directed dependency from word → board

3. **String enums**: All enums use lowercase string values for JSON serialization compatibility

4. **No logic**: These are pure type definitions. Validation, transformation, and business logic belong in the service and utils layers.
