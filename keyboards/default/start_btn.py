from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    KeyboardButton('✅Почати моніторинг'),
]

start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,)
start_kb.add(*btn)

