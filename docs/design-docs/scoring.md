# Scoring module design

## Purpose

Provides score calculation logic for words and sessions.

## Functions

### `calculate_word_score(word: str, word_type: WordType) -> int`

Calculates score for a single word.

**Formula:** `length(word) * multiplier(word_type)`

**Word Types:**
- `THEME_WORD`: 1x multiplier
- `SPANGRAM`: 2x multiplier  
- `NON_THEME`: 1x multiplier

### `calculate_session_score(session) -> int`

Calculates total session score by iterating through all discovered words.

**Algorithm:**
1. Iterate through `discovered_words.found_words`
2. Convert `DiscoveryType` to `WordType`
3. Calculate score for each word
4. Add scores for `spangrams_found`
5. Return total

## Implementation Notes

- Pure functions (no side effects)
- Uses `WordType` enum from types layer
- Converts `DiscoveryType` to `WordType` for scoring
