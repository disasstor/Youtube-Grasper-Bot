from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def content_types_kb(id, type):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("🎬 Video", callback_data=f"video {id} {type}"),
               InlineKeyboardButton("🎧 Audio", callback_data=f"audio {id} {type}"))
    return keyboard
