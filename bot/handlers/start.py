from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привіт! Я — частина екосистеми Markiian Hyshko Engineering Bureau.\n\n"
        "Готовий допомогти з проєктом або відповісти на питання.\n"
        "Напиши, що тебе цікавить."
    )