# -*- coding: utf-8 -*-

"""
Запрос на создание игр
"""

from modules.ORM.ListGames import ListGames


def create_games(data: dict) -> dict:
    """
    Запрос на создание игры в БД

    :param data: Информация о создаваемой игры полученная от клиента
    :return:
    """
    return ListGames.create_new_games(data)

