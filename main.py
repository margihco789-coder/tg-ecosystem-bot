"""
TG Ecosystem Bot — Main Entry Point
v160.0

Готовий до GitHub та production.
"""

import asyncio
import logging
import signal
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from core.config import settings
from integrations.user_bot_api import user_api

# handlers & middleware
from bot.handlers import start
from bot.middleware import setup_middleware


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

    # register handlers
    dp.include_router(start.router)

    # register middleware
    setup_middleware(dp)

    print("🚀 TG Ecosystem Bot v160.0 запущено")
    print("   Готовий до підключення твого API та VEXORA")

    stop_event = asyncio.Event()

    def _signal_handler():
        logging.info("Received stop signal, shutting down...")
        stop_event.set()

    loop = asyncio.get_running_loop()
    try:
        loop.add_signal_handler(signal.SIGINT, _signal_handler)
        loop.add_signal_handler(signal.SIGTERM, _signal_handler)
    except NotImplementedError:
        # Windows compatibility: loop.add_signal_handler may not be implemented
        pass

    try:
        if settings.USE_WEBHOOK and settings.WEBHOOK_URL:
            # Run webhook mode
            await dp.start_webhook(
                bot=bot,
                webhook_path=settings.WEBHOOK_PATH,
                webhook_url=settings.WEBHOOK_URL,
                host=settings.WEBHOOK_HOST,
                port=settings.WEBHOOK_PORT,
            )
        else:
            # Run polling in background and wait for stop_event
            polling_task = asyncio.create_task(dp.start_polling(bot))
            await stop_event.wait()
            polling_task.cancel()
            try:
                await polling_task
            except asyncio.CancelledError:
                pass
    finally:
        await user_api.close()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
