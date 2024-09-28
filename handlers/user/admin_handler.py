from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F
import os
import shutil

from filters.admin_filter import AdminFilter
from keyboard.keyboards import admin_keyboard
from bot_params import bot, Bot

from bot_params import ADMIN_IDS

admin_router = Router()

@admin_router.message(CommandStart(), AdminFilter())
async def admin_start_handler(message: Message) -> None:
    await message.answer("Salom admin!", reply_markup=admin_keyboard)

@admin_router.message(F.text == "Clean cache", AdminFilter())
async def clean_cache_command(message: Message) -> None:
    await manage_cache_and_notify_admins(message)

async def manage_cache_and_notify_admins(bot: Bot, message: Message, cache_dir='cache'):
    """
    Keshni boshqarish va boshliq adminlarga xabar yuborish funksiyasi.
    
    :param bot: Aiogram bot obyekti.
    :param message: Telegram xabari obyekti.
    :param cache_dir: Kesh fayllarini saqlaydigan papka nomi (default: 'cache').
    """
    # Kesh papkasining mavjudligini tekshiradi va agar mavjud bo'lmasa, yaratadi.
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        print(f"{cache_dir} papkasi yaratildi.")
    
    # Keshni tozalash
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)  # Papkani va uning ichidagi barcha fayllarni o'chirib tashlaydi
        print(f"{cache_dir} papkasi tozalandi.")
        
        # Boshliq admin uchun xabar yuborish
        try:
            await bot.send_message(ADMIN_IDS, f"{cache_dir} papkasi tozalandi.")
        except Exception as e:
            print(f"Adminga xabar yuborishda xato: {e}")
    else:
        print(f"{cache_dir} papkasi topilmadi, shuning uchun tozalash kerak emas.")
        # Boshliq admin uchun xabar yuborish
        try:
            await bot.send_message(ADMIN_IDS, f"{cache_dir} papkasi topilmadi.")
        except Exception as e:
            print(f"Adminga xabar yuborishda xato: {e}")
