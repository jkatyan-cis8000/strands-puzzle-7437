from typing import List
from src.types.board import Board, Cell
from src.types.word import WordType
from src.types.game import Discovery


ANSI_COLORS = {
    "reset": "\033[0m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
}


def render_board(board: Board, discovered: dict, partial: str = None) -> str:
    rows = []
    for row in board:
        cells = []
        for cell in row:
            letter = cell.letter
            cells.append(letter)
        rows.append(" ".join(cells))
    
    board_str = "\n".join(rows)
    
    if partial:
        board_str += f"\n\n{format_message(f'Current selection: {partial}')}"
    
    return board_str


def colorize_word(word: str, word_type: WordType) -> str:
    color_code = _get_color_for_type(word_type)
    reset = ANSI_COLORS["reset"]
    return f"{color_code}{word}{reset}"


def format_message(message: str) -> str:
    cyan = ANSI_COLORS["cyan"]
    reset = ANSI_COLORS["reset"]
    return f"{cyan}{message}{reset}"


def _get_color_for_type(word_type: WordType) -> str:
    colors = {
        WordType.THEME_WORD: ANSI_COLORS["yellow"],
        WordType.SPANGRAM: ANSI_COLORS["blue"],
        WordType.NON_THEME: ANSI_COLORS["green"],
    }
    return colors.get(word_type, ANSI_COLORS["reset"])
