from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Bu foydalanuvchilar uchun kinopkalar
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Buyurtma"), KeyboardButton(text="Mahsulotlar")]
    ],
    resize_keyboard=True
)
######################
