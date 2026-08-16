from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Simple /start handler"""
    await message.answer(
        "Привіт! Я — TG Ecosystem Bot. Використай цей бот як стартову точку."
    )
