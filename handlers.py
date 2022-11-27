from aiogram import types, Dispatcher


import controller
import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(controller.start, commands=['start'])
    dp.register_message_handler(controller.show_players, commands=['игроки'])
    dp.register_message_handler(controller.show_tables, commands=['столы'])
    dp.register_message_handler(controller.create_table, commands=['создать'])
    # dp.register_message_handler(controller.get_card, commands=['get'])
    # dp.register_message_handler(commands.stop, commands=['stop'])
    dp.register_message_handler(controller.next_turn, state=controller.Game.next_turn)
    # dp.register_callback_query_handler(callback='access', run_task=controller.seat_at_table)
    dp.register_callback_query_handler(controller.seat_at_table, text='access')

