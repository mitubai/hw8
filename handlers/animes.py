from bot import db
from aiogram import Router, F, types
from pathlib import Path

anime_router = Router()

@anime_router.callback_query(F.data == "animes")
async def make_order(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Боевик")
            ],
            [
                types.KeyboardButton(text="Романтика")
            ]
        ]
    )
    await callback.message.answer("Какое аниме хотите?", reply_markup=kb)


anime_categories = ("боевик", "романтика")
@anime_router.message(F.text.lower().in_(anime_categories))
async def show_dishes_of_category(message: types.Message):
    category = db.get_category_by_name(message.text)
    animes = db.get_dishes_by_cat_name(message.text)
    await message.answer(category[2])
    for anime in animes:
        file_path = Path(__file__).parent.parent / "images" / anime[3]
        file = types.FSInputFile(file_path)
        caption = f"Название{anime[1]}\nОписание: {anime[2]}"
        await message.answer_photo(file, caption=caption)
