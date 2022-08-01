from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def top_download_kb(top):
    buttons = []
    icon = {1: '🥇', 2: '🥈', 3: '🥉', 4: '🎖️', 5: '🎗️'}
    index = 1
    for item in top:
        item = item[0]
        buttons.append(InlineKeyboardButton(text=f'{icon.get(index)} Download Top {index}',
                                            callback_data=f"top {item.file_unique_id}"))
        index += 1
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard
