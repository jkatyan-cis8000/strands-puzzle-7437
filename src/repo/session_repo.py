import json
import os
from typing import Optional
from dataclasses import dataclass

from src.types.game import PuzzleSession, GameState, PlayerDiscovery, Discovery, DiscoveryType


SESSIONS_FILE = "sessions.json"


def save_session(session: PuzzleSession, filepath: str = SESSIONS_FILE) -> None:
    session_data = _session_to_dict(session)
    _save_to_file(session_data, filepath)


def load_session(session_id: str, filepath: str = SESSIONS_FILE) -> Optional[PuzzleSession]:
    if not os.path.exists(filepath):
        return None
    
    data = _load_from_file(filepath)
    if session_id in data:
        return _dict_to_session(data[session_id])
    return None


def _session_to_dict(session: PuzzleSession) -> dict:
    return {
        "game_state": session.game_state.value,
        "found_words": {word: {"found": d.found, "word_type": d.word_type.value} for word, d in session.discovered_words.found_words.items()},
        "spangrams_found": list(session.discovered_words.spangrams_found),
        "score": session.score,
        "hints_available": session.hints_available
    }


def _dict_to_session(data: dict) -> PuzzleSession:
    found_words = {
        word: Discovery(found=d["found"], word_type=DiscoveryType(d["word_type"]))
        for word, d in data["found_words"].items()
    }
    return PuzzleSession(
        game_state=GameState(data["game_state"]),
        discovered_words=PlayerDiscovery(
            found_words=found_words,
            spangrams_found=set(data["spangrams_found"])
        ),
        score=data["score"],
        hints_available=data["hints_available"]
    )


def _save_to_file(data: dict, filepath: str) -> None:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            existing = json.load(f)
    else:
        existing = {}
    
    existing.update(data)
    
    with open(filepath, 'w') as f:
        json.dump(existing, f, indent=2)


def _load_from_file(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)
