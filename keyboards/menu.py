from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/rooms")]
        ],
        resize_keyboard=True
    )

def rooms_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Общая комната")],
            [KeyboardButton(text="Бийск")],
            [KeyboardButton(text="Администрация")]
        ],
        resize_keyboard=True
    )
