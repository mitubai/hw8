import asyncio
import logging
from aiogram import Bot

from bot import bot, dp, on_startup
from handlers.start import start_router
from handlers.animes import anime_router


async def main():
    dp.include_router(start_router)
    dp.include_router(anime_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())