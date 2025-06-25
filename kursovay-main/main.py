import asyncio
from aiogram import Bot, Dispatcher
from handlers import router

async def test():
    bot = Bot(token='7008255063:AAFMaQBv_O5HMxFVmeN5gQuP4cTURGRBtqc')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(test())
    except KeyboardInterrupt:
        print('Бот выключен')
