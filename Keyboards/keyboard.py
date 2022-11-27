

from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
serach_players = KeyboardButton('/игроки')
search_tables = KeyboardButton('/столы')


start_keyboard.add(serach_players, search_tables)