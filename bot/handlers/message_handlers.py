from aiogram import types, Dispatcher
from bot.db.user import check_user
from bot.keyboards.content_types_kb import content_types_kb
from bot.utils.extractor_id import get_id, regex_youtube
from bot.utils.extractor_thumb import get_thumb
from bot.utils.extractor_title import get_title


async def help_cmd(message: types.Message):
    await message.delete()
    await check_user(message)
    await message.answer(
        f"Hello { message.from_user.full_name } I'm Youtube Grasper Bot!\n"
        f"You can use me to grab videos from Youtube.\n"
        f"Send me a link to a video and I'll send you a link to download it."
    )


async def input_url(message: types.Message):
    id_data = get_id(message.text)
    if id_data is None:
        await message.reply('Invalid URL, try again.')
        return
    await message.delete()
    title = get_title(id_data['id'], id_data['type'])
    thumb = get_thumb(id_data['id'], id_data['type'])
    await message.answer_photo(photo=thumb,
                               caption=f'<b>{title}</b>\n\n<i>Please select type of content</i>',
                               reply_markup=content_types_kb(id_data['id'], id_data['type']))


def register_msg(dp: Dispatcher):
    dp.register_message_handler(help_cmd, commands=['start', 'help', 'info', 'старт', 'помощь', 'инфо'])
    dp.register_message_handler(input_url, regexp=regex_youtube)
