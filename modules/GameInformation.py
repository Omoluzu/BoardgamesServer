# -*- coding: utf-8 -*-

"""
Запрос на обновление списка активныз игр
"""
import os
import csv
import json

from modules.ORM.ListGames import ListGames


def game_information(data: dict):
    """
    Запрос информации об игре
    :return: 
    """

    path_games = ListGames.get_path_games(id_games=data['game_id'])
    game_info = None

    if os.path.isfile(path_games):
        with open(path_games) as f:
            reader = csv.reader(f)
            game_info = list(reader)[-1][1]

    return {
        **ListGames.get_games_info(data['game_id']),
        "command": "game_info",
        "game_id": data['game_id'],
        "game_info": json.loads(game_info) if game_info else None
    }
