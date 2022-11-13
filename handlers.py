from aiogram import types, Dispatcher


import controller
import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    # dp.register_message_handler(controller.get_card, commands=['get'])
    # dp.register_message_handler(commands.stop, commands=['stop'])
    dp.register_message_handler(controller.next_turn, state=controller.Game.next_turn)

