# Hints module design

## Purpose

Manages hint unlocking and retrieval based on game progress.

## Functions

### `check_hint_unlock(session) -> tuple(bool, Hint)`

Checks if a hint should be unlocked based on non-theme words found.

**Logic:**
1. Count non-theme words found (excluding spangrams)
2. If count > 0 and divisible by HINT_THRESHOLD, unlock hint
3. Returns `(True, hint)` or `(False, empty_hint)`

### `get_next_hint(session) -> Hint`

Returns the next hint based on most recent theme word.

**Algorithm:**
1. Find all discovered theme words
2. Return hint referencing the latest one
3. If no theme words, return empty hint

## Configuration

- `HINT_THRESHOLD = 3` (from config/settings.py)
- Unlocks hint every 3 non-theme words

## Implementation Notes

- Hint content references the word to help player
- Returns Hint namedtuple with content, word_type, and word fields
- Pure functions with no side effects
