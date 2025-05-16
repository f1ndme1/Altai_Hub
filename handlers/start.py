from aiogram import Router
from aiogram.types import Message
from .rooms import rooms_keyboard

router = Router()

@router.message(lambda message: message.text == "/start")
async def cmd_start(message: Message):
    await message.answer("👋 Привет! Выберите комнату:", reply_markup=rooms_keyboard())
