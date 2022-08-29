"""Test bot related functionality"""

from src.bot import run_bot


def test_bot() -> None:
    run_bot(is_daemon=True)
