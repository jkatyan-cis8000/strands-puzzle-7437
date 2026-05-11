import dataclasses
from typing import NamedTuple, Tuple
from enum import Enum

from src.types.board import Position, Direction
from src.types.game import PuzzleSession, GameState, PlayerDiscovery
from src.config.settings import GRID_ROWS, GRID_COLS
from src.types.board import Board
from src.ui.display import (
    display_board,
    display_score,
    display_hints_remaining,
    display_themes,
    clear_screen,
)


class Command(Enum):
    MOVE = "move"
    SELECT = "select"
    SUBMIT = "submit"
    HINT = "hint"
    QUIT = "quit"
    INVALID = "invalid"


class CommandData(NamedTuple):
    direction: Direction = None
    position: Position = None
    confirm: bool = False


def parse_input(user_input: str) -> Tuple[Command, CommandData]:
    user_input = user_input.strip().lower()

    if user_input in ("quit", "q", "exit", "x"):
        return (Command.QUIT, CommandData())

    if user_input in ("hint", "h", "?"):
        return (Command.HINT, CommandData())

    if user_input == "submit" or user_input == "s":
        return (Command.SUBMIT, CommandData(confirm=True))

    parts = user_input.split()
    if len(parts) < 2:
        return (Command.INVALID, CommandData())

    if parts[0] in ("move", "m"):
        if len(parts) < 3:
            return (Command.INVALID, CommandData())
        try:
            row = int(parts[1])
            col = int(parts[2])
            direction = Direction(parts[3]) if len(parts) > 3 else None
            return (Command.MOVE, CommandData(position=Position(row, col), direction=direction))
        except (ValueError, KeyError):
            return (Command.INVALID, CommandData())

    if parts[0] in ("select", "s"):
        if len(parts) < 3:
            return (Command.INVALID, CommandData())
        try:
            row = int(parts[1])
            col = int(parts[2])
            return (Command.SELECT, CommandData(position=Position(row, col)))
        except ValueError:
            return (Command.INVALID, CommandData())

    return (Command.INVALID, CommandData())


def handle_input(session: PuzzleSession, command: Tuple[Command, CommandData]) -> PuzzleSession:
    cmd, data = command

    if cmd == Command.QUIT:
        return dataclasses.replace(session, game_state=GameState.LOST)

    if cmd == Command.HINT:
        if session.hints_available > 0:
            return dataclasses.replace(session, hints_available=session.hints_available - 1)
        return session

    if cmd == Command.SUBMIT:
        return session

    return session


def display_game_status(session: PuzzleSession) -> None:
    clear_screen()
    display_score(session.score)
    display_hints_remaining(session.hints_available)
    display_themes("fruits", 0)


def main_loop() -> None:
    print("Welcome to Strands!")
    print("Commands: move <row> <col> [direction], select <row> <col>, submit, hint, quit\n")

    session = PuzzleSession(
        game_state=GameState.PLAYING,
        discovered_words=PlayerDiscovery(found_words={}, spangrams_found=set()),
        score=0,
        hints_available=3,
    )

    board = _create_sample_board()

    while session.game_state == GameState.PLAYING:
        display_board(board, session.discovered_words)
        display_game_status(session)

        user_input = input("Enter command: ")
        command = parse_input(user_input)
        session = handle_input(session, command)

        if command[0] == Command.QUIT:
            print("Game ended.")
            break

    print(f"Final Score: {session.score}")


def _create_sample_board() -> Board:
    from src.types.board import Cell, Board

    cells: list[list[Cell]] = []
    for row in range(GRID_ROWS):
        cell_row: list[Cell] = []
        for col in range(GRID_COLS):
            letter = chr(65 + ((row * GRID_COLS + col) % 26))
            cell_row.append(Cell(letter=letter, row=row, col=col))
        cells.append(tuple(cell_row))
    return Board(tuple(cells))


if __name__ == "__main__":
    main_loop()
