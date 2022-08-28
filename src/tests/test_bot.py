import os

from src.bot import run_bot

token = os.environ["TOKEN"]

run_bot(token)
