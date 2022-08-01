from sqlalchemy.exc import NoResultFound
from bot.db.models import User


async def check_user(message):
    id_user = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    lang = message.from_user.language_code
    user = await get_user_by_id(id_user)
    if user is None:
        await create_user(id_user, username, first_name, last_name, lang)
    if user is not None and user.username != username or user.first_name != first_name or user.last_name != last_name:
        await update_user(id_user, username, first_name, last_name)
    return user


async def create_user(id_user, username, first_name, last_name, lang):
    user = User(id=id_user, username=username, first_name=first_name, last_name=last_name, lang=lang)
    await User.create(user)


async def update_user(id_user, username, first_name, last_name):
    await User.update(id_user, username, first_name, last_name)


async def get_user_by_id(id_user):
    try:
        user = await User.get(id_user)
        return user
    except NoResultFound:
        return None


########################################################################################################################


async def get_premium_users():
    premium_user = await User.get_premium()
    return premium_user


async def add_premium(id_user, premium_date):
    await User.add_premium(id_user, premium_date)


async def del_premium(id_user):
    await User.del_premium(id_user)


########################################################################################################################

async def get_banned_users():
    banned_user = await User.get_banned()
    return banned_user


async def add_ban(id_user, banned, banned_reason):
    await User.add_ban(id_user, banned, banned_reason)


async def del_ban(id_user):
    await User.del_ban(id_user)


########################################################################################################################

async def update_user_dl_count(id_user):
    user = await get_user_by_id(id_user)
    await User.update_dl_count(id_user, user.dl_count + 1)

########################################################################################################################
