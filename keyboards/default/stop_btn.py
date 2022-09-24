from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    KeyboardButton('❌Зупинити моніторинг', ),
]

stop_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
stop_kb.add(*btn)

