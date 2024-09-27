from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot_params import ADMIN_IDS, bot

buyurtma_olish_router = Router()

@buyurtma_olish_router.message(F.text == "Buyurtma")
async def buyurtma_olish_handler(message: Message, state: FSMContext):
    buyutma_matni = message.text
    user_name = message.from_user.full_name
    admin_message = f"Yangi buyurtma!\n\nFoydalanuvchi: {user_name}\nBuyurtma: {buyutma_matni}"

    for admin in ADMIN_IDS:
        try:
            await bot.send_message(admin, admin_message)
        except Exception as e:
            print(f"Adminга xabar yuborishda xatolik: {e}")

    await message.answer("Buyurtmangiz qabul qilindi. Rahmat!")
    await state.clear()
