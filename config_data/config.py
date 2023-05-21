from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str              # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str| None) -> Config:
    '''Добавляет из файла env данные и возвращает экземпляр класса Config'''
    # Создаём экземпляр класса Env
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env(path)
    # Возвращаем экземпляр класса Config и наполняем его данными из переменных окружения.
    return Config(tg_bot=TgBot(token=env('bot_token_konfa')))

