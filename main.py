from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import logging
import asyncio
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from handlers.handler import command_router
from handlers.message_handlers import message_router
async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    await bot.set_my_commands(commands=[
        BotCommand(command='start', description="start/restart bot"),
        BotCommand(command='help', description="Manual for this bot")
    ])
    dp = Dispatcher()
    dp.include_router(command_router)
    dp.include_router(message_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
