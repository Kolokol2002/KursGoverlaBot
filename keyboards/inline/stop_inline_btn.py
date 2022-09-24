from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_btn_stop = InlineKeyboardButton('❌Зупинити моніторинг', callback_data='stop')
inline_stop = InlineKeyboardMarkup().add(inline_btn_stop)
