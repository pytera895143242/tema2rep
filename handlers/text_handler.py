from aiogram import types
from misc import dp,bot
import asyncio

@dp.message_handler(content_types='text')
async def all_other_messages(message: types.message):
    print(message)