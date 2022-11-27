import random

from aiogram import types
import controller
from Classes.deck import Deck
from bot_create import bot
from Classes import player


async def start(message: types.Message):
    ME = player.Player(message)
    await bot.send_message(ME.get_id(), ME.greetings())


# async def start(message: types.Message):
#     my_player = player.Player(message)
#     my_enemy = None
#     if main_game.is_empty():
#         main_game.add(my_player)
#         print('Зарегался')
#     else:
#         my_enemy = main_game.get_players()
#         print(f'{my_player.info()} играет против {my_enemy.info()}')
#         deck = Deck(52)
#         deck.shuffle()
#         await controller.player_turn(message, deck, my_player, my_enemy)
# async def create_table(message, main_game, bet, *args):
#     for player_id in args:
#         for player in main_game.players_list():
#             if player.get_id() == int(player_id):
#                 await bot.send_message(player.get_id(), 'Вас приглашают за стол')
