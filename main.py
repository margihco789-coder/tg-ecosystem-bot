"""
TG Ecosystem Bot — Main Entry Point
v160.0

Готовий до GitHub та production.
"""

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from core.config import settings
from integrations.user_bot_api import user_api


async def main():
    logging.basicConfig(
        level=logging.INFO if not settings.DEBUG else logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    # TODO: підключи handlers
    # from bot.handlers import start, lead
    # dp.include_router(start.router)
    # dp.include_router(lead.router)

    # TODO: підключи middleware
    # TODO: підключи webhook з сайту (якщо потрібно)

    print("🚀 TG Ecosystem Bot v160.0 запущено")
    print("   Готовий до підключення твого API та VEXORA")

    try:
        await dp.start_polling(bot)
    finally:
        await user_api.close()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())