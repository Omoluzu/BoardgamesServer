# -*- coding: utf-8 -*-

"""
Запрос на создание игр
"""

from modules.ORM.ListGames import ListGames


def create_games(data: dict):
    """
    Запрос на создание игры в БД

    :param data: Информация о создаваемой игры полученная от клиента
    :return:
    """
    message_chat = {
        "type": "message",
        "message": f"Пользователь {data['user']}: Создал игру {data['ru']}",
        "user": "System"
    }

    return ListGames.create_new_games(data), message_chat

