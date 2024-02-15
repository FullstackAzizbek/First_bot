from aiogram import Router, F
from aiogram.types import Message
from keyboar.all_keyboards import get_category
from utils.database import Database
from config import DB

message_router = Router()
db = Database(DB)

@message_router.message(F.text == 'Categories')  # Changed 'Categories' to 'categories'
async def category_handler(message: Message):
    await message.answer(
        text="Select category, please...",
        reply_markup=get_category()
        )

@message_router.message(F.text.in_({'Smartphones', 'Notebooks', 'Watchs', 'Cars'}))
async def product_handler(message: Message):
    cats = db.get_categories()
    for cat in cats:
        if message.text == cat[1]:
            products = db.get_products(cat[0])
            break
    await message.answer_photo(
        photo=products[0][4],
        caption=f"<b>{products[0][1]}</b>\n{products[0][3]}\nPrice: ${products[0][2]}"
    )
