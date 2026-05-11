# UI layer
# User-facing surfaces (CLI)

from src.ui.display import (
    clear_screen,
    display_board,
    display_score,
    display_hints_remaining,
    display_themes,
)

from src.ui.cli import (
    parse_input,
    handle_input,
    display_game_status,
    main_loop,
)
