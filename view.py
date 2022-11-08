# Сюда все функции отправляющие сообщения

from aiogram import types

from bot import bot

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, приветик!\n'
        f'Добро пожаловать в игру!')

async def bye(message: types.Message):
        await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, спасибо за игру.\n'
        f'Пока.')

async def candy(message: types.Message):
    number = message.text
    if 0 < int(number) < 29:
        print(number)
    else:
        await bot.send_message(message.from_user.id,'Какие то неправильности. Введите корректное количество конфет:')
    