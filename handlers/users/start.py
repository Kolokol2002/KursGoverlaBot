import asyncio
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from selenium import webdriver
from selenium.webdriver.common.by import By

from keyboards.inline import inline_stop
from loader import dp

from keyboards.default import start_kb, minutes_kb, stop_kb
from states.start import For_Start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=start_kb)




@dp.message_handler(Text(equals=['✅Почати моніторинг'], ignore_case=True))
async def traking(message: types.Message):
    await message.answer('Виберіть інтервал моніторингу', reply_markup=minutes_kb)
    await For_Start.start.set()


@dp.message_handler(state=For_Start.start)
async def start(message: types.Message, state: FSMContext):


    exchange_after = list


    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--headless')
    while 1:
        minute = (re.findall('\d+', message.text))[0]
        try:

            driver = webdriver.Chrome(
                executable_path= '~/KursGoverlaBot/chromedriver_linux',
                options=options)
            driver.get("https://goverla.ua/")

            res = driver.find_elements(By.CLASS_NAME, 'value__absolute')

            exchange = [str(num.text) for num in res]

            if exchange[0] != exchange_after[0] or exchange[1] != exchange_after[1]:
                await message.answer(f'🇺🇸 - {exchange[0]}/{exchange[1]}\n'
                                     f'🇪🇺 - {exchange[2]}/{exchange[3]}',
                                     reply_markup=inline_stop)
                exchange_after = exchange

        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
        if len(minute) == 2:
            await asyncio.sleep(int(minute) * 60)
        elif len(minute) == 1:
            await asyncio.sleep(int(minute) * 60 * 60)


@dp.callback_query_handler(text='stop', state='*')
async def next_keyboard(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Моніторинг зупинено!', reply_markup=start_kb)

    await state.finish()

