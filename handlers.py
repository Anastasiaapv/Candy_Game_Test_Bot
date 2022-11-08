# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands

def registed_handlers(dp: Dispatcher):
    dp.register_message_handler (commands.start, commands=['start'])
    dp.register_message_handler (commands.finish, commands=['finish'])
    # dp.registed_message_handlers (commands.set_count, commands=['set_count'])

    dp.register_message_handler (commands.getNumber)