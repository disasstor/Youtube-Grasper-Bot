import os
from aiogram import types, Dispatcher
from bot.db.file import create_file, check_file, update_dl_count
from bot.db.user import update_user_dl_count
from bot.keyboards.quality_generator_kb import quality_generator_kb
from bot.utils.downloader_video import downloader
from bot.utils.downloader_data import get_data
from bot.utils.extractor_video import get_video
from bot.utils.sender_file import send_file


async def call_video_data(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_title = callback_query.message.caption.split('\n')[0]
    content_type = callback_query.data.split(' ')[0]
    id = callback_query.data.split(' ')[1]
    url_type = callback_query.data.split(' ')[2]
    await callback_query.message.edit_caption(caption=f'<b>{message_title}</b>\n\n<i>Collecting data...</i>')
    await callback_query.message.edit_caption(
        caption=f'<b>{message_title}</b>\n\n<i>Please select quality of media</i>',
        reply_markup=quality_generator_kb(get_video(id, content_type, url_type), url_type, id, content_type)
    )


async def call_download(callback_query: types.CallbackQuery):
    await callback_query.answer()
    print(callback_query.data)
    message_title = callback_query.message.caption.split('\n')[0]
    await callback_query.message.edit_caption(
        caption=f'<b>{message_title}</b>\n\n<i>Please wait a few seconds</i>'
    )
    itag = callback_query.data.split(' ')[1]
    id = callback_query.data.split(' ')[2]
    url_type = callback_query.data.split(' ')[3]
    content_type = callback_query.data.split(' ')[4]
    quality = callback_query.data.split(' ')[5]

    video_data = get_data(id, itag, url_type)
    await callback_query.message.delete()
    for title, author, thumbnail, filename, id in video_data:
        file = await check_file(id, quality)
        if file:
            await send_file(callback_query, content_type, file.title, file.author, file.thumb, file.file_id)
            await update_dl_count(file.file_id, file.dl_count)
            await update_user_dl_count(callback_query.from_user.id)
        else:
            result_dl = downloader(id, url_type, itag)
            while result_dl:
                break
            file = await send_file(callback_query, content_type, title, author, thumbnail, open(filename, 'rb'))
            await create_file(file.audio.file_unique_id, file.audio.file_id, title, author, thumbnail, quality, id)
            await update_user_dl_count(callback_query.from_user.id)
            os.remove(filename)



    '''
    file = await check_file(id, quality)
    if file:
        await send_file(callback_query, content_type, file.title, file.author, file.thumb, file.file_id)
        await update_dl_count(file.file_id, file.dl_count)
        await update_user_dl_count(callback_query.from_user.id)
    else:
        video_data = get_data(id, itag, url_type)
        result_dl = downloader(id, url_type, itag)
        while result_dl:
            break
        await callback_query.message.delete()
        for title, author, thumbnail, filename in video_data:
            file = await send_file(callback_query, content_type, title, author, thumbnail, open(filename, 'rb'))
            await create_file(file.audio.file_unique_id, file.audio.file_id, title, author, thumbnail, quality, id)
            await update_user_dl_count(callback_query.from_user.id)
            os.remove(filename)
'''

def register_cb(dp: Dispatcher):
    dp.register_callback_query_handler(call_video_data, lambda x: x.data.startswith('video'))
    dp.register_callback_query_handler(call_video_data, lambda x: x.data.startswith('audio'))
    dp.register_callback_query_handler(call_download, lambda x: x.data.startswith('dl'))
