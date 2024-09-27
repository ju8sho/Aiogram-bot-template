from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.text_decorations import html_decoration as hd

from bot_params import ADMIN_IDS, bot
from state.buyurtma import BuyurtmaState

buyurtma_olish_router = Router()



@buyurtma_olish_router.message(F.text == "Buyurtma")
async def buyurtma_olish_handler(message: Message, state: FSMContext):
    # Foydalanuvchidan buyurtma matnini so'raymiz
    text = (
        f"{hd.bold('Buyurtmangizni yozing:')}\n"
        f"{hd.code('Misol uchun:\n1kg go\'sht kerak, suvagi va yog\'i ko\'proq bo\'lsin, Palonchi ko\'chasi, palonchi uy')}"
    )

    await message.answer(text, parse_mode="HTML")
    await state.set_state(BuyurtmaState.matn_kiritish)  # Foydalanuvchini state ga o'tkazamiz


@buyurtma_olish_router.message(BuyurtmaState.matn_kiritish)
async def buyurtma_matni_qabul_qilish(message: Message, state: FSMContext):

# Foydalanuvchining buyurtma matnini qabul qilamiz
    buyurtma_matni = message.text
    user_fullname = message.from_user.full_name or "Ism ko'rsatilmagan"
    user_username = message.from_user.username
    user_id = message.from_user.id

    # Agar username mavjud bo'lsa, to'liq ism bilan birga ko'rsatamiz
    if user_username:
        user_link = f"{user_fullname} (@{user_username})"
    else:
        # Agar username mavjud bo'lmasa, faqat to'liq ismni ko'rsatamiz
        user_link = hd.link(user_fullname, f"tg://user?id={user_id}")


    admin_message = (
        f"{hd.bold('Yangi buyurtma!')}\n\n"
        f"{hd.italic('Foydalanuvchi:')} {user_link}\n"
        f"{hd.bold('Buyurtma matni:')}\n{hd.pre(buyurtma_matni)}"
    )

    # Adminlarga xabar yuboramiz
    for admin in ADMIN_IDS:
        try:
            await bot.send_message(admin, admin_message, parse_mode="HTML")
        except Exception as e:
            print(f"Adminга xabar yuborishda xatolik: {e}")

    # Foydalanuvchiga tasdiqlash xabarini yuboramiz


    await message.answer(
        f"{hd.bold('Buyurtmangiz qabul qilindi.')}\n"
        f"{hd.italic('Admin siz bilan bog\'lanadi!')}",
        parse_mode="HTML"
    )
    await state.clear()  # State ni tozalaymiz