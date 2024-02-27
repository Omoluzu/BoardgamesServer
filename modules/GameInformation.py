# -*- coding: utf-8 -*-

"""
Запрос на обновление списка активныз игр
"""
import os
import csv
import json

from modules.ORM.ListGames import ListGames


def game_information(data: dict, test=False):
    """
    Запрос информации об игре
    :return: 
    """

    path_games = ListGames.get_path_games(id_games=data['game_id'])

    if test:
        path_games = os.path.join('..', '..', '..', '..', path_games)

    if os.path.isfile(path_games):
        with open(path_games, encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            (
                step_id,
                game_info,
                server_info
            ) = list(reader)[-1]

    return {
        **ListGames.get_games_info(data['game_id']),
        "command": "game_info",
        "game_id": data['game_id'],
        "game_info": json.loads(game_info) if game_info else None,
        "server_info": json.loads(server_info) if server_info else None
    }
