from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import DB
from utils.database import Database
import asyncio

db = Database(DB)

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Categories")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Press this button ...",
    one_time_keyboard=True
)

def get_category() -> ReplyKeyboardMarkup:
    categories = db.get_categories()
    cats = []
    for cat in categories:
        cats.append(
            KeyboardButton(text=cat[1])
        )
    markup = ReplyKeyboardMarkup(
        keyboard=[
            cats
        ],
    resize_keyboard=True,
    input_field_placeholder="Please select category...",
    one_time_keyboard=True
    )
    return markup