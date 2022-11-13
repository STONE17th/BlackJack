from Classes import game
import handlers
from bot_create import dp
from aiogram import executor


async def on_startup(_):
    print('Бот')

handlers.registred_handlers(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


