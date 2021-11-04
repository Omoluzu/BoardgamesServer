# -*- coding: utf-8 -*-

"""
Запрос на создание игр
"""

from modules.ORM.ListGames import ListGames


def create_games(data: dict) -> tuple:
    """
    Запрос на создание игры в БД

    :param data: Информация о создаваемой игры полученная от клиента
    :return:
    """
    message_chat = {
        "command": "message",
        "message": f"Пользователь {data['user']}: Создал игру {data['ru']}",
        "user": "System"
    }
    ListGames.create_new_games(data)

    return ListGames.get_current_action_games(), message_chat

