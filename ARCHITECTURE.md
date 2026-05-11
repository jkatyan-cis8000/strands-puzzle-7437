# Strands Puzzle Architecture

## Overview

This document describes the layered architecture for the Strands puzzle implementation.

## Layers

### `src/types/`
Pure type definitions for the domain model. No logic, only data structures.
- `board.py`: Grid and cell types
- `game.py`: Game state and session types
- `word.py`: Word discovery and validation types
- `hint.py`: Hint system types

### `src/config/`
Constants, settings, and environment configuration.
- `settings.py`: Game constants (grid size, themes, etc.)
- `themes.py`: Themed word lists for different puzzle themes

### `src/repo/`
Data access layer - file-based persistence for puzzles and sessions.
- `puzzle_repo.py`: Load puzzles from disk
- `session_repo.py`: Save/load game sessions

### `src/providers/`
Cross-cutting concerns - scoring, hint management, UI helpers.
- `scoring.py`: Scoring logic for words
- `hints.py`: Hint unlocking and management
- `renderer.py`: ANSI color rendering for terminal UI

### `src/utils/`
Pure helper functions, no internal imports.
- `grid.py`: Grid manipulation helpers
- `validation.py`: Input validation helpers

### `src/service/`
Business logic - core game rules and state transitions.
- `game_engine.py`: Core game loop, word discovery, spangram detection
- `board_generator.py`: Board generation and validation
- `word_finder.py`: Find all valid words on a board

### `src/runtime/`
Application lifecycle, orchestration, wiring layers together.
- `main.py`: Entry point, coordinates the game
- `session_manager.py`: Manages active game sessions

### `src/ui/`
User-facing surfaces - terminal CLI.
- `cli.py`: Command-line interface
- `display.py`: Board rendering and user feedback

## Dependencies

```
types → config → repo → service → runtime → ui
                     ↑              ↑
                  providers ──────┘
                  
utils is leaf - no internal imports
```

## Entry Points

- `src/runtime/main.py`: Application entry point
- `src/ui/cli.py`: User interface layer
