import asyncio
import logging
import sys
from aiogram import Dispatcher

from filters.admin_filter import AdminFilter
from handlers import routers_list
from bot_params import bot
from commands import set_bot_commands


async def main() -> None:
    await set_bot_commands()

    dp = Dispatcher()
    dp.include_routers(*routers_list)
    # dp.message.filter(AdminFilter())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())