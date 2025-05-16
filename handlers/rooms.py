from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from db.database import join_room

router = Router()

def rooms_keyboard():
    keyboard = [
        [KeyboardButton(text="Общая")],
        [KeyboardButton(text="Бийск")],
        [KeyboardButton(text="Администрация")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)  # без one_time_keyboard

@router.message(lambda m: m.text in ["Общая", "Бийск", "Администрация"])
async def process_room_choice(message: Message):
    join_room(message.from_user.id, message.text)
    await message.answer(f"✅ Вы вошли в комнату: {message.text}")
    # НЕ возвращаем ничего — просто не даём chat-хендлеру срабатывать на эту же строчку
