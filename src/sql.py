"""This file will contain SQL related functions"""
import sqlite3

from __init__ import root_dir

# Fetch the workspaces' resources folder.
resources_path: str = root_dir + "\\resources"
records_path: str = resources_path + "\\records.db"


def create_message(guild_id: str, message: str) -> None:
    """
    This function will create a new message for the provided guild
    :param guild_id: The guild that the message was sent in.
    :param message: The contents of the message.
    """
    with sqlite3.connect(records_path) as connection:
        cursor: sqlite3.Cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO messages VALUES(?, ?)", [guild_id, message])
        except sqlite3.Error as error:
            print("An error occurred while creating a new message.", error)


def batch_create_message(guild_id: str, messages: [str]) -> None:
    """
    This function will batch create the provided messages.
    :param guild_id: The messages' associated guild.
    :param messages: A list of the message contents.
    """
    [create_message(guild_id, message) for message in messages]


def read_messages(guild_id: str) -> [str]:
    """
    This function will fetch all the messages from the provided guild id.
    :param guild_id: The guild containing the messages.
    """
    with sqlite3.connect(records_path) as connection:
        cursor: sqlite3.Cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM messages where id=?", [guild_id])
        except sqlite3.Error as error:
            print("An error occurred while reading messages.", error)


def initialize() -> None:
    """
    This function will initialize the records' database.
    It will insert the schema if it doesn't already exist.
    """
    with sqlite3.connect(records_path) as connection:
        cursor: sqlite3.Cursor = connection.cursor()

        try:
            cursor.execute(
                "CREATE TABLE if not exists messages(id TEXT, message TEXT);"
            )
        except sqlite3.Error as error:
            print("An error occurred while creating schema.", error)
