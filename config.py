import logging
from environs import Env
from dataclasses import dataclass

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand


@dataclass
class Hidden:
    bot_token: str
    admin_id: list[int]
    yatoken: str


def load_config(path: str = None):
    env = Env()
    env.read_env()
    return Hidden(
        admin_id=list(map(int, env.list("ADMIN_ID"))),
        bot_token=env.str("BOT_TOKEN"),
        yatoken=env.str("YATOKEN"),
    )


logging.basicConfig(level=logging.INFO)

hidden_vars = load_config('..env')

bot = Bot(token=hidden_vars.bot_token)
dp = Dispatcher()

commands = [
    BotCommand(
        command='start',
        description='Начало работы бота'
    ),
    BotCommand(
        command='admin_message',
        description='Написать админу'
    )
]
