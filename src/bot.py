"""Contains Discord bot related functionality. It'll bridge the python markov chain framework to the user."""

from typing import Any

import discord

from markov import Markov


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
        self.markov: Markov = (
            Markov()
        )  # Create a unique markov object for this instance.
        super().__init__(
            intents=intents, **options
        )  # Make sure to call the init from our superclass.

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


def run_bot(token: str) -> None:
    """
    This function will create and run a new Discord bot.
    :param token: The unique token associated with the bot.
    """
    # Create our Discord client and run it.
    # I decided to use a simple one liner here, as there is not much going on.
    DiscordClient(intents=discord.Intents.none()).run(token)
