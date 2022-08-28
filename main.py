"""This file will contain the entrypoint. It'll start the Discord bot."""

from configparser import ConfigParser

from src.bot import run_bot
from src.sql import initialize


def main() -> None:
    """
    This function is the application's entrypoint.
    """
    # First, we have to fetch our config.
    config: ConfigParser = ConfigParser()
    config.read("config.properties")  # Read the config.properties file.

    # Fetch the associated configurations.
    discord_token: str = config["discord"]["token"]

    # Initialize the SQL.
    initialize()

    # Finally, start the bot.
    run_bot(discord_token)


if __name__ == "__main__":
    main()
