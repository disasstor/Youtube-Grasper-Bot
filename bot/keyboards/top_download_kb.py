from aiogram.types import InlineKeyboardMarkup as ikm
from aiogram.types import InlineKeyboardButton as ikb

from bot.templates.message import top_cmd_icons


def top_download_kb(top):
    buttons = [ikb(text=f'{top_cmd_icons.get(index)} Top {index}', callback_data=f"top {item.file_unique_id}") for index, item in enumerate(top, start=1)]
    keyboard = ikm(row_width=2)
    keyboard.add(*buttons)
    return keyboard
