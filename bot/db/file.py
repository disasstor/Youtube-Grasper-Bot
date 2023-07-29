from sqlalchemy.exc import NoResultFound
from bot.db.models import File


async def check_file(yt_id, quality):
    try:
        file = await File.get_by_yt_id_and_quality(yt_id, quality)
        return file
    except NoResultFound:
        return None


async def create_file(file_unique_id, file_id, title, author, thumb, quality, youtube_id):
    file = File(file_unique_id=file_unique_id,
                file_id=file_id,
                title=title,
                author=author,
                thumb=thumb,
                quality=quality,
                youtube_id=youtube_id)
    await File.create(file)


async def get_file_by_file_unique_id(file_unique_id):
    try:
        file = await File.get(file_unique_id)
        return file
    except NoResultFound:
        return None


async def update_dl_count(file_id, dl_count):
    await File.update_dl_count(file_id, dl_count+1)


async def get_top_5():
    return await File.get_top_5()


async def get_file_by_file_id(file_id):
    try:
        file = await File.get_by_id(file_id)
        return file
    except NoResultFound:
        return None
