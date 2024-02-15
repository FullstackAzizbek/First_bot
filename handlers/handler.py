from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboar.all_keyboards import kb_start

command_router = Router()


@command_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        text="Assalomu Alaykum!\nHush kelibsiz!",
        reply_markup=kb_start
        )

@command_router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(text="Do you need help!\nFollow this <a href='https://portfolioazizbek.netlify.app/'>link</a>")