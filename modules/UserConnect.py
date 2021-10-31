# -*- coding: utf-8 -*-

"""
Запрос на создание игр
"""


def user_connect(info) -> dict:
    """
    Инициализация подключения пользователя в систему

    :return:
        Приветственное сообщение
    """

    message = {
        "command": "message",
        "message": f"Пользователь {info['user']} вошел в систему",
        "user": "System"
    }

    return message
