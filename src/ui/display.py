import os

from src.config.settings import GRID_ROWS, GRID_COLS
from src.types.board import Board, Cell
from src.types.game import PlayerDiscovery


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def display_board(board: Board, discovered_words: PlayerDiscovery, partial_word=None) -> None:
    print("\n  ", end="")
    for col in range(GRID_COLS):
        print(f"   {col} ", end="")
    print()

    for row_idx, row in enumerate(board):
        print(f"{row_idx} ", end="")
        for cell in row:
            cell_key = f"{cell.row},{cell.col}"
            is_discovered = any(
                cell_key in [f"{p.row},{p.col}" for p in path.positions]
                for found in discovered_words.found_words.keys()
                for path in [None]
            )
            if partial_word and cell_key in partial_word:
                print(f" [{cell.letter}]", end="")
            elif is_discovered:
                print(f" *{cell.letter}*", end="")
            else:
                print(f"  {cell.letter} ", end="")
        print()
    print()


def display_score(score: int) -> None:
    print(f"Score: {score}\n")


def display_hints_remaining(hint_count: int) -> None:
    print(f"Hints remaining: {hint_count}\n")


def display_themes(theme_name: str, words_remaining: int) -> None:
    print(f"Theme: {theme_name}")
    print(f"Words remaining: {words_remaining}\n")
