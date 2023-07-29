from bot.utils.extractor_thumb import get_thumb_buffer


async def send_file(call_back_query, content_type, title, author, thumb_url, file):
    file_unique_id = ''
    file_id = ''
    if content_type == 'video':
        file = await call_back_query.message.answer_video(
            video=file,
            thumb=get_thumb_buffer(thumb_url)
        )
        file_unique_id = file.video.file_unique_id
        file_id = file.video.file_id
    elif content_type == 'audio':
        file = await call_back_query.message.answer_audio(
            audio=file,
            thumb=get_thumb_buffer(thumb_url),
            title=title,
            performer=author
        )
        file_unique_id = file.audio.file_unique_id
        file_id = file.audio.file_id
    file_dict = {'file_unique_id': file_unique_id, 'file_id': file_id}
    return file_dict
