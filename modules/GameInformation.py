# -*- coding: utf-8 -*-

"""
Запрос на обновление списка активныз игр
"""

from modules.ORM.ListGames import ListGames


def game_information(data: dict):
    """
    Запрос информации об игре
    :return: 
    """

    print("Запрос на информацию по игре")

    path_games = ListGames.get_path_games(id_games=data['game_id'])

    print(path_games)

