"""Test SQL related functionality"""

import os
import sqlite3

from src.__init__ import root_dir
from src.sql import (
    batch_create_message,
    create_message,
    initialize,
    read_messages,
    records_path,
)

messages_to_write: [str] = [
    "Lorem ipsum dolor sit amet.",
    "Mauris vel arcu tempus, ullamcorper urna a, maximus enim.",
    "Mauris sagittis neque id metus bibendum maximus.",
]


def test_initialize() -> None:
    """
    Test the initialize function in sql.py by ensuring the resources
    directory and message table are successfully created
    """
    initialize()

    resources_directory_exists = os.path.exists(f"{root_dir}\\resources")

    assert resources_directory_exists

    with sqlite3.connect(records_path) as connection:
        cursor: sqlite3.Cursor = connection.cursor()

        # Ensure the messages table was created successfully
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='messages'"
        )
        result = cursor.fetchone()

        assert result is not None


def test_read_write_workflow() -> None:
    """
    Test the read and write functionality of sql.py
    """
    create_message("test_guild", messages_to_write[0])
    batch_create_message("test_guild", messages_to_write[1:])

    messages = read_messages("test_guild")
    messages_present = dict.fromkeys(messages_to_write, False)

    for message in messages:
        message = message[0]

        assert message in messages_present

        messages_present[message] = True

    assert all(
        is_message_present is True
        for is_message_present in list(messages_present.values())
    )
