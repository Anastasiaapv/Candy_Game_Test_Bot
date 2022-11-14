from aiogram import types
from bot import bot
import model 
import random

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, приветик!\n'
        f'Добро пожаловать в игру!\n'
        f'У меня на столе лежит 150 конфет, каждый из нас за один ход может брать не больше 28 конфет.\n'
        f'Выигрывает тот кто сделает последний ход.\n'
        f'Если хочешь начать игру нажми /game \n'
        f'Если игра надоест жми /finish \n')


async def stol(message: types.Message):
    model.player = random.randint(0,2)  
    if model.player:
        await message.answer('Первый ход за тобой. Напоминаю что всего у нас 150 конфет. Введи количество конфет которое хочешь взять от 1 до 28.')
    else:
        model.count = model.candy%29
        model.candy -= model.count
        await message.answer(f'Так выпало что я хожу первым, пожалуй возьму {model.count} конфет. На столе осталось {model.candy} конфет.\n'
                                'Теперь ходи ты!')

async def bye(message: types.Message):
        await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, спасибо за игру. Захочешь ещё поиграть набирай /game.\n'
        f'Пока.')
