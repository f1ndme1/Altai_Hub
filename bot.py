import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from keep_alive import keep_alive
keep_alive()
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from handlers import start, rooms
from db.database import init_db, get_user_room, get_users_in_room

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7772194130:AAGRgTwUUNKMrIo-uag0SEJmUx69DLqZIic")
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(rooms.router)

# Исключаем команду /start, кнопку выбора комнаты и сами названия комнат
CHAT_FILTER = (
    F.text
    & ~F.text.startswith("/")
    & ~F.text.in_(["Общая", "Бийск", "Администрация"])
)

@dp.message(CHAT_FILTER)
async def handle_chat(message: Message):
    room = get_user_room(message.from_user.id)
    if room:
        users = get_users_in_room(room)
        for user_id in users:
            if user_id != message.from_user.id:
                try:
                    await bot.send_message(
                        user_id, 
                        f"[{room}] {message.from_user.full_name}: {message.text}"
                    )
                except Exception as e:
                    logging.warning(f"Не удалось отправить сообщение {user_id}: {e}")
    else:
        await message.answer("❗ Вы не выбрали комнату. Нажмите /start и выберите комнату.")

async def main():
    init_db()
    logging.info("✅ Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
