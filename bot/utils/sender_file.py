from bot.db.file import update_dl_count
from bot.db.user import update_user_dl_count
from bot.utils.extractor_thumb import get_thumb_buffer


async def send_file(call_back_query, content_type, title, author, thumb_url, file):
    if content_type == 'video':
        file = await call_back_query.message.answer_video(
            video=file,
            thumb=get_thumb_buffer(thumb_url),
            caption=f'<b>{title}</b>\n\n<i>{author}</i>'
        )
    elif content_type == 'audio':
        file = await call_back_query.message.answer_audio(
            audio=file,
            thumb=get_thumb_buffer(thumb_url),
            title=title,
            performer=author
        )
    return file
