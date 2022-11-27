from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

invite_keyboard = InlineKeyboardMarkup(row_width=1).\
    add(InlineKeyboardButton(text='Принять', callback_data='access'),
        InlineKeyboardButton(text='Отклонить', callback_data='cancel'))
