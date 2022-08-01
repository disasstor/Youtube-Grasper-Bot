from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def quality_generator_kb(video_data, url_type, id, content_type):
    buttons = []
    if url_type == 'video':
        quality = video_data['quality']
        itag = video_data['itag']
        data = list(map(list, zip(*[quality, itag])))
        for quality, itag in data:
            buttons.append(
                InlineKeyboardButton(
                    quality,
                    callback_data=f'dl {itag} {id} {url_type} {content_type} {quality}'
                )
            )
    elif url_type == 'playlist':
        print(video_data)
        quality = video_data[0]['quality']
        itag = video_data[0]['itag']
        data = list(map(list, zip(*[quality, itag])))
        for quality, itag in data:
            buttons.append(
                InlineKeyboardButton(
                    quality,
                    callback_data=f'dl {itag} {id} {url_type} {content_type} {quality}'
                )
            )
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard
