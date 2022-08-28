"""Contains Discord bot related functionality. It'll bridge the python markov chain framework to the user."""

import os
from threading import Thread
from typing import Any, Optional

import discord

from src.markov import Markov


class DiscordClient(discord.Client):
    """
    This class will contain the framework for the Discord client.
    It will contain the common event definitions.
    """

    def __init__(self, *, intents: discord.Intents, **options: Any) -> None:
        """
        This method will construct a new DiscordClient object. It will also call the superclass constructor method.
        :param intents: The intents of the bot.
        :param options: Other miscellaneous options.
        """
        self.thread: Optional[Thread] = None
        self.markov: Markov = (
            Markov()
        )  # Create a unique markov object for this instance.
        super().__init__(
            intents=intents, **options
        )  # Make sure to call the init from our superclass.

    def threaded_run_bot(self, token: str, is_daemon: bool = False) -> None:
        """
        This method runs the Discord bot on a new thread.
        :param token: The Discord bot token.
        :param is_daemon: A boolean indicating whether the thread should be a daemon
        """
        self.thread = Thread(target=self.run, args=(token,))
        self.thread.daemon = is_daemon

        self.thread.start()

    async def on_ready(self) -> None:
        """
        This method will be invoked upon the ready event.
        It'll let the user know that the bot is ready.
        """
        print(f"Logged into {self.user.name}!")

    async def on_message(self, message: discord.Message) -> None:
        """
        This method will be invoked once a message is sent.
        :param message: The events associated message object.
        """
        pass


def run_bot(is_daemon: bool = False) -> DiscordClient:
    """
    This function will create and run a new Discord bot.
    :param is_daemon: A boolean indicating whether the thread should be a daemon
    """
    # Create our Discord client and run it.
    # I decided to use a simple one liner here, as there is not much going on.
    token: str = os.environ["TOKEN"]
    client: DiscordClient = DiscordClient(intents=discord.Intents.none())
    client.threaded_run_bot(token, is_daemon)

    return client
