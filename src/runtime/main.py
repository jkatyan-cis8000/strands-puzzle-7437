from src.service import (
    load_puzzle,
    generate_board,
    create_session,
    save_session,
    process_command
)
from src.providers import scoring, hints, renderer


def main() -> None:
    puzzle_data = load_puzzle()
    words = set(puzzle_data.words)
    spangrams = set(puzzle_data.spangrams) if 'spangrams' in puzzle_data else set()
    
    board = generate_board(list(words), list(spangrams))
    
    session = create_session(puzzle_data)
    _run_game_loop(session, puzzle_data, board)


def _run_game_loop(session, puzzle_data, board) -> None:
    from src.ui.display import (
        clear_screen,
        display_board,
        display_score,
        display_hints_remaining,
        display_themes
    )
    from src.types.game import GameState
    
    words = set(puzzle_data.words)
    spangrams = set(puzzle_data.spangrams) if 'spangrams' in puzzle_data else set()
    
    while session.game_state == GameState.PLAYING:
        clear_screen()
        
        display_themes(
            puzzle_data.theme,
            len(words) - len(session.discovered_words.found_words)
        )
        display_board(board, session.discovered_words)
        display_score(session.score)
        display_hints_remaining(session.hints_available)
        
        try:
            command = input("\n> ").strip().upper()
            
            if command == "HINT":
                unlocked, hint = hints.check_hint_unlock(session)
                if unlocked:
                    print(f"\nHint: {hint.content}")
                else:
                    print("\nNo hint available yet.")
                continue
            
            if command == "QUIT":
                session.game_state = GameState.LOST
                break
            
            process_command(command, session, words, spangrams)
            save_session(session)
        
        except EOFError:
            session.game_state = GameState.LOST
            break
