from dataclasses import dataclass
from os import getenv

from aiogram.bot.api import TelegramAPIServer


@dataclass
class Bot:
    token: str
    server_api: TelegramAPIServer


@dataclass
class DB:
    host: str
    port: int
    db_name: str
    user: str
    password: str


@dataclass
class Config:
    bot: Bot
    db_url: str


def read_config():
    return Config(
        bot=Bot(token=getenv("BOT_TOKEN"),
                server_api=TelegramAPIServer.from_base(getenv("SERVER_BOT_API"))),
        db_url=f"postgresql+asyncpg://"
               f"{getenv('DB_USER')}:"
               f"{getenv('DB_PASSWORD')}@"
               f"{getenv('DB_HOST')}:"
               f"{getenv('DB_PORT')}/"
               f"{getenv('DB_NAME')}",
        )

