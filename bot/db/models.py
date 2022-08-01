from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update
from bot.db.base import Base, async_db_session


class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)  # Telegram ID
    lang = Column(String(2), default="en")  # Language code
    username = Column(String(50), default='None')  # Telegram username
    first_name = Column(String(50), default='None')  # Telegram first name
    last_name = Column(String(50), default='None')  # Telegram last name
    dl_count = Column(BigInteger, default=0)  # Download count
    banned = Column(Boolean, default=False)  # Is user banned
    banned_reason = Column(String(200))  # Reason for ban
    premium_date = Column(DateTime)  # Date of premium

    @classmethod
    async def create(cls, user):
        async_db_session.add(user)
        await async_db_session.commit()

    @classmethod
    async def get(cls, id_user):
        query = select(cls).where(cls.id == id_user)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result

    @classmethod
    async def update(cls, id_user, username, first_name, last_name):
        query = (
            sqlalchemy_update(User)
                .where(User.id == id_user)
                .values(username=username)
                .values(first_name=first_name)
                .values(last_name=last_name)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def update_dl_count(cls, id_user, dl_count):
        query = (
            sqlalchemy_update(User)
                .where(User.id == id_user)
                .values(dl_count=dl_count)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def add_ban(cls, id_user, banned, banned_reason):
        query = (
            sqlalchemy_update(User)
                .where(User.id == id_user)
                .values(banned=banned)
                .values(banned_reason=banned_reason)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def del_ban(cls, id_user):
        query = (
            sqlalchemy_update(User)
                .where(User.id == id_user)
                .values(banned=False)
                .values(banned_reason=None)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get_banned(cls):
        query = select(cls).where(cls.banned == True)
        results = await async_db_session.execute(query)
        return results.fetchall()

    @classmethod
    async def add_premium(cls, id_user, premium_date):
        query = (
            sqlalchemy_update(User)
                .where(User.id == id_user)
                .values(premium_date=premium_date)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def del_premium(cls, id_user):
        query = (
            sqlalchemy_update(User)
                .where(User.id == id_user)
                .values(premium_date=None)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get_premium(cls):
        query = select(cls).where(cls.premium_date is not None)
        results = await async_db_session.execute(query)
        return results.fetchall()


class File(Base):
    __tablename__ = 'files'
    file_unique_id = Column(String(100), primary_key=True)  # Telegram file unique id
    file_id = Column(String(100))  # Telegram file id
    title = Column(String(200))  # Title of file
    author = Column(String(100))  # Author of file
    thumb = Column(String(100))  # Thumbnail of file
    quality = Column(String(10))  # Quality of file
    youtube_id = Column(String(20))  # YouTube id of file
    dl_count = Column(BigInteger, default=1)  # Download count

    @classmethod
    async def create(cls, file):
        async_db_session.add(file)
        await async_db_session.commit()

    @classmethod
    async def get(cls, file_unique_id):
        query = select(cls).where(cls.file_unique_id == file_unique_id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result

    @classmethod
    async def get_by_id(cls, file_id):
        query = select(cls).where(cls.file_id == file_id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result

    @classmethod
    async def get_by_yt_id_and_quality(cls, youtube_id, quality):
        query = select(cls).where(cls.youtube_id == youtube_id).where(cls.quality == quality)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result

    @classmethod
    async def get_top_5(cls):
        query = select(cls).order_by(cls.dl_count.desc()).limit(5)
        results = await async_db_session.execute(query)
        return results.fetchall()

    @classmethod
    async def update(cls, file_unique_id, file_id, title, author, thumb, quality, youtube_id):
        query = (
            sqlalchemy_update(File)
                .where(File.file_unique_id == file_unique_id)
                .values(file_id=file_id)
                .values(title=title)
                .values(author=author)
                .values(thumb=thumb)
                .values(quality=quality)
                .values(youtube_id=youtube_id)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def update_dl_count(cls, file_id, dl_count):
        query = (
            sqlalchemy_update(File)
                .where(File.file_id == file_id)
                .values(dl_count=dl_count)
                .execution_options(synchronize_session="fetch")
        )
        await async_db_session.execute(query)
        await async_db_session.commit()
