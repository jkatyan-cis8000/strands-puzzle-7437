# Config Layer Design

## Overview

The config layer provides centralized configuration and theme data for the Strands puzzle game.

## Files

### settings.py

Contains all game-wide constants:

- **GRID_ROWS**: 6 - Number of rows in the puzzle grid
- **GRID_COLS**: 8 - Number of columns in the puzzle grid
- **MIN_WORDS**: 4 - Minimum number of theme words required for a valid puzzle
- **MAX_WORDS**: 8 - Maximum number of theme words allowed in a puzzle
- **HINT_THRESHOLD**: 3 - Number of non-theme words found before hints are unlocked
- **DEFAULT_PUZZLES_FILE**: "puzzles.json" - Default file for storing puzzles

### themes.py

Provides pre-defined themed word lists for different categories:

- **FRUITS**: 8 fruit-themed words (APPLE, BANANA, CHERRY, DATE, GRAPE, KIWI, LIME, MANGO)
- **ANIMALS**: 8 animal-themed words (CAT, DOG, FISH, BIRD, LION, TIGER, BEAR, WOLF)
- **COLORS**: 8 color-themed words (RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, BLACK, WHITE)

The **THEMES** dictionary provides convenient access to all themes by category name.

## Design Decisions

1. **Separation of concerns**: Settings and themes are separated into different files since they serve different purposes (configuration vs. game content)

2. **Hardcoded values**: All constants are defined directly in settings.py for clarity and ease of modification

3. **Theme structure**: Themes use consistent naming (uppercase, plural category names as keys) for predictability

4. **Word count**: Each theme provides 8 words to allow flexibility in puzzle generation while meeting the MIN_WORDS/MAX_WORDS constraints

## Usage

```python
from src.config import settings, themes

# Access grid dimensions
rows = settings.GRID_ROWS
cols = settings.GRID_COLS

# Access theme words
fruit_words = themes.FRUITS
all_themes = themes.THEMES
```
