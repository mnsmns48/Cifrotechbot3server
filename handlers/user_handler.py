from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_ = Router()


async def start(m: Message):
    await m.answer('user mode')


def register_user_handlers():
    user_.message.register(start, CommandStart())
