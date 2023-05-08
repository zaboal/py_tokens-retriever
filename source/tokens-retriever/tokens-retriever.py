from os import environ
from logging import warning
from typing import List


class Tokens:
    """Получение для обёрток переменных окружения, они должны соответствовать формату `ПАКЕТ_ИМЯМОДУЛЯАПИ`."""

    def __init__(self, retrieve: List[str]) -> None:
        for name in retrieve:
            api_name = name.upper()
            package_name = __name__.upper()
            environ_name = package_name + "_" + api_name + "_TOKEN"
            token = environ.get(environ_name)
            if token == str(None):
                warning(f"Токен «{environ_name}» не получен.")
            else:
                setattr(self, str(name.lower()), str(token))
