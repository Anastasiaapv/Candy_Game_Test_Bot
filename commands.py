# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types
import view
from bot import bot


async def start(message: types.Message):
    await view.greetings(message)
        

async def finish(message: types.Message):
       await view.bye(message)

async def getNumber(message: types.Message):

    await view.candy(message)
  