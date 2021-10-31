# -*- coding: utf-8 -*-

"""
Запрос на инициализацию подключения пользователя в систему
"""
from modules.ORM.ListGames import ListGames


def user_connect(info) -> tuple:
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

    return message, ListGames.get_current_action_games()
