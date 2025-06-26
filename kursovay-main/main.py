import asyncio
from aiogram import Bot, Dispatcher
from handlers import router

async def test():
    bot = Bot(token='токен бота')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(test())
    except KeyboardInterrupt:
        print('Бот выключен')
