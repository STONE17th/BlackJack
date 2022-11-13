import random

from aiogram import types
import controller
from Classes.deck import Deck
from bot_create import dp
from controller import main_game
from Classes import player


async def start(message: types.Message):
    my_player = player.Player(message)
    my_enemy = None
    if main_game.is_empty():
        main_game.add(my_player)
        print('Зарегался')
    else:
        my_enemy = main_game.get_players()
        print(f'{my_player.info()} играет против {my_enemy.info()}')
        deck = Deck(52)
        deck.shuffle()
        await controller.player_turn(message, deck, my_player, my_enemy)


