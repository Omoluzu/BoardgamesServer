# -*- coding: utf-8 -*-

"""
Запрос на обновление списка активныз игр
"""

import os

from modules.ORM.ListGames import ListGames


def game_information(data: dict):
    """
    Запрос информации об игре
    :return: 
    """

    path_games = ListGames.get_path_games(id_games=data['game_id'])

    if not os.path.isfile(path_games):
        return {
            "command": "game_info",
            "game_id": data['game_id'],
            "game_info": None
        }


