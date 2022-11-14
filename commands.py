from aiogram import types
import view
from bot import bot
import model
import random

async def start(message: types.Message):
    await view.greetings(message)
        
async def game(message: types.Message):
    await view.stol(message)  

async def finish(message: types.Message):
       await view.bye(message)

async def getNumber(message: types.Message):
    model.count = message.text
    if model.count.isdigit():
        model.count = int(model.count)

        if 0 < model.count < 29:
            model.candy -= model.count

            if model.candy == 150 and model.player == 2:
                await message.answer('Хочешь начать новую игру? Жми /game')

            else:
                if 28*2+1 >= model.candy > 29:   
                    await message.answer(f'На столе осталось {model.candy} конфет')
                    model.count = model.candy - 27
                    model.candy -=  model.count
                    await message.answer(f'Я беру {model.count} конфет. На столе осталось {model.candy}')

                elif model.candy == 0:
                    await message.answer('Ура! Ты победил!\nЯ конечно рад за тебя, но не от всего сердца')
                    await message.answer('Хочешь ещё поиграть? жми /game.\n')
                    model.candy = 150

                elif model.candy <= 28:
                    if model.count > model.candy + model.count:
                        model.candy += model.count
                        await message.answer(f'У нас всего {model.candy} конфет. Подумай!\n'
                                                'И походи ещё раз')

                    else:
                        await message.answer(f'Я беру {model.candy} конфет. Хаха вот я и победил!')
                        await message.answer('Хочешь ещё поиграть? жми /game.\n')
                        model.candy = 150

                else:
                    await message.answer(f'Осталось {model.candy} конфет')
                    if model.player == 0:
                        model.count = random.randint(1, 28)

                    else:
                        model.count = 29 - model.count
                    model.candy -=  model.count
                    await message.answer(f'Я беру {model.count} конфет. На столе осталось {model.candy}')

        else:
            await message.answer('Какие то неправильности. Введи корректное количество конфет:')

    else:
       await message.answer('Я таких команд не знаю!\n'
                            'Давай лучше поиграем, жми /game\n') 
