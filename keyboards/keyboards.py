from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Наше аниме", callback_data="animes"),
            ]
        ]
    )
    return kb