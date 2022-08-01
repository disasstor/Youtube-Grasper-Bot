import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeDefault

from bot.config_reader import Config, read_config
from bot.db.base import async_db_session
from bot.handlers.callback_handlers import register_cb
from bot.handlers.message_handlers import register_msg
from bot.updatesworker import get_handled_updates_list


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start command"),
        BotCommand(command="top", description="View top-5 downloads")
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def init_app():
    await async_db_session.init()
    # await async_db_session.create_all()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    config: Config = read_config()

    await init_app()
    bot = Bot(token=config.bot.token, server=config.bot.server_api, parse_mode="HTML")
    dp = Dispatcher(bot)

    register_cb(dp)
    register_msg(dp)

    await set_bot_commands(bot)

    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    logging.error("Bot stopped!")
