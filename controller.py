from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import Keyboards.inline_keyboards
from Classes import game, player
from Keyboards import keyboard
from bot_create import bot, dp


class Game(StatesGroup):
    next_turn = State()


main_game = game.Game()


async def start(message: types.Message):
    ME = player.Player(message)
    for play in main_game.players_list():
        if play.get_dis_id() == message.from_user.id:
            break
    else:
        main_game.add(ME)
    await bot.send_message(message.from_user.id, ME.greetings(), reply_markup=keyboard.start_keyboard)


async def show_tables(message: types.Message):
    await bot.send_message(message.from_user.id, main_game.show_tables())


async def show_players(message: types.Message):
    await bot.send_message(message.from_user.id, main_game.show_players())


async def create_table(message: types.Message):
    data = message.text.split()
    table_id = main_game.get_table_id()
    main_game.create_table(message.from_user.id, int(data[1]))
    for player_id in data[2:]:
        for player in main_game.players_list():
            if player.get_id() == int(player_id):
                await bot.send_message(player.get_dis_id(),
                                       f'{message.from_user.first_name} приглашает тебя за {table_id} стол.\nСтавки: {data[1]}',
                                       reply_markup=Keyboards.inline_keyboards.invite_keyboard)


async def seat_at_table(callback: types.CallbackQuery):
    data = callback.message.text.split('\n')
    # print(callback.from_user.first_name)
    # print(callback.from_user.id)
    # print(data[0].split()[-2])
    # print(data[1].split()[-1])
    main_game.seat(callback.from_user.id, int(data[0].split()[-2]))


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


@dp.message_handler(state=Game.next_turn)
async def next_turn(message: types.Message, player, state: FSMContext):
    if message.from_user.id == player.id:
        if message.text.equals('y'):
            return True
        else:
            await bot.send_message(player.id, 'Отправь "y" - чтобы взять еще карту'
                                              'или "n" - чтобы остановиться')
    else:
        await state.finish()
        return False
