from typing import Any
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Update, data: dict[str, Any]):
        # Простий логгер обновлень — можна розширити під свої потреби
        try:
            logger.debug("Incoming update: %s", event)
        except Exception:
            pass
        return await handler(event, data)


def setup_middleware(dp):
    """Register middleware on the Dispatcher.

    Keep this function as a single place to register all middleware so it's
    easy to extend later.
    """
    # У aiogram можна реєструвати middleware для всіх оновлень або для певного маршруту
    # Приклад (залежить від версії aiogram):
    try:
        dp.update.middleware.register(LoggingMiddleware())
    except Exception:
        # Якщо інтерфейс іншої версії aiogram, реєстрацію можна помістити сюди
        logger.debug("Could not register middleware via dp.update.middleware.register — skip for now")

