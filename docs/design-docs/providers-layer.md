# Providers layer design

## Overview

The providers layer handles cross-cutting concerns that are used across multiple parts of the application. These are utility functions that don't belong to a specific domain layer but are needed throughout the codebase.

## Files

### scoring.py

Handles score calculation for words and sessions.

**Functions:**

- `calculate_word_score(word, word_type) -> int`  
  Calculates score for a single word based on length and type.
  
- `calculate_session_score(session) -> int`  
  Calculates total score for a session by summing all discovered words.

**Scoring Rules:**
- Base score = word length
- Multipliers:
  - Theme word: 1x
  - Spangram: 2x
  - Non-theme: 1x

### hints.py

Manages hint unlocking and retrieval.

**Functions:**

- `check_hint_unlock(session) -> tuple(bool, Hint)`  
  Checks if a hint should be unlocked (every 3 non-theme words found).
  Returns (should_unlock, hint).

- `get_next_hint(session) -> Hint`  
  Returns the next available hint based on most recently found theme word.

**Hint Logic:**
- Hint unlocks after every 3 non-theme words (configurable via HINT_THRESHOLD)
- Hints reference the most recent theme word found

### renderer.py

Handles ANSI color rendering for terminal display.

**Functions:**

- `render_board(board, discovered, partial=None) -> str`  
  Renders the game board as a formatted string.
  
- `colorize_word(word, word_type) -> str`  
  Returns word with ANSI color codes based on type.
  
- `format_message(message) -> str`  
  Formats a message with cyan color for display.

**Color Mapping:**
- Theme word: Yellow
- Spangram: Blue
- Non-theme: Green
- Messages: Cyan

## Design Decisions

1. **Purity**: All functions are pure where possible, avoiding side effects.
2. **Imports**: Providers may import from types, config, utils, and other providers.
3. **Separation**: Each provider handles a single concern (score, hints, rendering).
4. **Extensibility**: The structure allows easy addition of new providers (e.g., validation, save/load).
