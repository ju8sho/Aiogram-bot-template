from aiogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, getenv("ADMIN_IDS", "").split(",")))
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))