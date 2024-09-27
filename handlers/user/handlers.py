from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html, Router, F
from aiogram.filters import StateFilter

from filters.admin_filter import AdminFilter

handler_routers = Router()

@handler_routers.message(CommandStart(), AdminFilter())
async def admin_start_handler(message: Message) -> None:
    await message.answer("Salom admin!")

@handler_routers.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@handler_routers.message(F.text, StateFilter(None))
async def bot_echo(message: Message):
    text = ["Echo no state.", "Xabar:", message.text]

    await message.answer("\n".join(text))
