from aiogram import types, Dispatcher

from bot.db.file import get_top_5
from bot.db.user import check_user
from bot.keyboards.content_types_kb import content_types_kb
from bot.keyboards.top_download_kb import top_download_kb
from bot.utils.extractor_id import get_id, regex_youtube
from bot.utils.extractor_thumb import get_thumb
from bot.utils.extractor_title import get_title


async def help_cmd(message: types.Message):
    await message.delete()
    await check_user(message)
    await message.answer(f"🎉 Hey <b>{message.from_user.full_name}</b>!\n\n"
                         f"<i>I'm Youtube Grasper Bot 🤖!\n"
                         f"I can help you to grab videos from Youtube.\n"
                         f"Send me a link to a video and I will send you a link to download it.</i>")


async def input_url(message: types.Message):
    id_data = get_id(message.text)
    if id_data is None:
        await message.reply('<i>🗿 Invalid URL, try again.</i>')
        return
    await message.delete()
    await message.answer_photo(photo=get_thumb(id_data['id'], id_data['type']),
                               caption=f"<b>🎸 {get_title(id_data['id'], id_data['type'])}</b> 📽️\n\n"
                                       f"<i>🤖 What do you need to download?</i>",
                               reply_markup=content_types_kb(id_data['id'], id_data['type']))


async def get_top_videos(message: types.Message):
    top = await get_top_5()
    icon = {1: '🥇', 2: '🥈', 3: '🥉', 4: '🎖️', 5: '🎗️'}
    index = 1
    text_msg = '🏆 Top 5 downloads:\n\n'
    for item in top:
        item = item[0]
        text_msg += f'{icon.get(index)} {index}. {item.title} {item.quality} | Downloaded {item.dl_count} times 🚀\n\n'
        index += 1
    await message.answer(text=text_msg, reply_markup=top_download_kb(top))


def register_msg(dp: Dispatcher):
    dp.register_message_handler(help_cmd, commands=['start', 'help', 'info', 'старт', 'помощь', 'инфо'])
    dp.register_message_handler(get_top_videos, commands=['top', 'топ'])
    dp.register_message_handler(input_url, regexp=regex_youtube)
