from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Classes import game
from bot_create import bot, dp
from aiogram import types

class Game(StatesGroup):
    next_turn = State()

@dp.message_handler(state=Game.next_turn)
async def next_turn(message: types.Message, player, state: FSMContext):
    if message.from_user.id == player.id:
        if message.text.equals('y'):
            return True
        else:
            await bot.send_message(player.id, 'Отправь "y" - чтобы взять еще карту'
                                              'или "n" - чтобы сотановиться')
    else:
        await state.finish()
        return False

main_game = game.Game()

async def player_turn(message, deck, player, enemy):
    choice = 1
    while choice:
        await get_card(deck, player, enemy)


    await bot.send_message(enemy.id, 'Твой противник закончил ход')
    while choice:
        await get_card(deck, enemy, player)
        if not dp.register_message_handler(lambda message: next(message, enemy)):
            choice = 0
    await bot.send_message(player.id, 'Твой противник закончил ход')
    if player.get_value() > enemy.get_value():
        await bot.send_message(player.id, f'Ты победил! У тебя {player.get_value()} против {enemy.get_value()}')
        await bot.send_message(enemy.id, f'Ты проиграл! У тебя {enemy.get_value()} против {player.get_value()}')


async def get_card(deck, player, enemy, state: FSMContext):
    player_card = deck.take()
    player.take_card(player_card)
    await bot.send_message(enemy.id, 'Твой противник взял карту')
    player.set_value(player_card.get_value())
    await bot.send_message(player.id, f'Ты взял {player_card.info()}\n'
                                      f'У тебя {player.get_value()} очков')
    if player.get_value() > 21:
        await bot.send_message(player.id, 'Перебор')
        player_summa = 0
        return player_summa
    await bot.send_message(player.id, 'Берем еще карту? (y/n)')
    await state.set_state(Game.next_turn)

async def next(message: types.Message, player):
    if message.from_user.id == player.id:
        if message.text.equals('y'):
            return True
        else:
            await bot.send_message(player.id, 'Отправь "y" - чтобы взять еще карту'
                                              'или "n" - чтобы сотановиться')


class Game(StatesGroup):
    next_turn = State()

@dp.message_handler(state=Game.next_turn)
async def next_turn(message: types.Message, player, state: FSMContext):
    if message.from_user.id == player.id:
        if message.text.equals('y'):
            return True
        else:
            await bot.send_message(player.id, 'Отправь "y" - чтобы взять еще карту'
                                              'или "n" - чтобы сотановиться')
    else:
        await state.finish()
        return False
