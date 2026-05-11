from src.types.game import PuzzleSession, GameState, PlayerDiscovery, Discovery, DiscoveryType
from typing import Dict


_sessions: Dict[str, PuzzleSession] = {}


def create_session(puzzle_data: dict) -> PuzzleSession:
    """Create a new game session."""
    session = PuzzleSession(
        game_state=GameState.PLAYING,
        discovered_words=PlayerDiscovery(
            found_words={},
            spangrams_found=set()
        ),
        score=0,
        hints_available=3
    )
    session_id = str(id(session))
    _sessions[session_id] = session
    return session


def get_session(session_id: str) -> PuzzleSession:
    """Get session by ID."""
    return _sessions.get(session_id)


def save_session(session: PuzzleSession) -> None:
    """Save current session state."""
    session_id = str(id(session))
    _sessions[session_id] = session


def resume_session(session_id: str) -> PuzzleSession:
    """Resume a saved session."""
    return _sessions.get(session_id)
