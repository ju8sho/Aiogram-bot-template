import asyncio
import logging
import sys


from aiogram import Dispatcher

from filters.admin_filter import AdminFilter
from handlers import routers_list
from bot_params import bot
from commands import set_bot_commands


# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
dp.include_routers(*routers_list)

dp.message.filter(AdminFilter())

async def main() -> None:
    await set_bot_commands()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())