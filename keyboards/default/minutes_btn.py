from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    KeyboardButton('✅10 мин'),
    KeyboardButton('✅30 мин'),
    KeyboardButton('✅1 час'),
    KeyboardButton('✅2 часа'),
    KeyboardButton('✅3 часа'),
    KeyboardButton('✅4 часа'),

]

minutes_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, )
minutes_kb.add(*btn)

