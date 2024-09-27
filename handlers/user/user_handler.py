from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F

from filters.admin_filter import AdminFilter

admin_router = Router()

@admin_router.message(CommandStart(), AdminFilter())
async def admin_start_handler(message: Message) -> None:
    await message.answer("Salom admin!")

