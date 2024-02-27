from bot.utils.extractor_thumb import get_thumb_buffer
from aiogram.types import InputFile, CallbackQuery


async def send_file(call_back_query: CallbackQuery,
                    content_type: str,
                    title: str,
                    author: str,
                    thumb_url: str,
                    file: InputFile) -> dict:
    file_unique_id = ''
    file_id = ''
    if content_type == 'video':
        file = await call_back_query.message.answer_video(
            video=file,
            thumb=get_thumb_buffer(media_thumb_url=thumb_url, form='circle')
        )
        file_unique_id = file.video.file_unique_id
        file_id = file.video.file_id
    elif content_type == 'audio':
        file = await call_back_query.message.answer_audio(
            audio=file,
            thumb=get_thumb_buffer(media_thumb_url=thumb_url, form='circle'),
            title=title,
            performer=author
        )
        file_unique_id = file.audio.file_unique_id
        file_id = file.audio.file_id
    file_dict = {'file_unique_id': file_unique_id, 'file_id': file_id}
    return file_dict
