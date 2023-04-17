# -*- coding: utf-8 -*-

"""
Запрос на подтверждение создание игры
"""

import os
import csv
import json

from modules.ORM.ListGames import ListGames
from modules.GameInformation import game_information
from src.games.azul.view import started_configure


def approved_games(data):
    print(data)

    game_info = ListGames.get_games_info(games_id=data['game_id'])
    game_data = started_configure(games_config=game_info['games_config'])

    print(game_data)

    # path_games = ListGames.get_path_games(id_games=data['game_id'])

    # if not os.path.exists(os.path.dirname(path_games)):
    #     os.mkdir(os.path.dirname(path_games))

    # create_data_games = [
    #     ["ID", "INFO GAMES"],
    #     [1, json.dumps(data['info_game'])]
    # ]

    # with open(path_games, 'w') as f:
    #     writer = csv.writer(f)
    #     for row in create_data_games:
    #         writer.writerow(row)

    return {
        "command": "game_info",
        "game_id": data['game_id'],
        "games": 'azul',
        "game_info": game_data.get('players')
    }
    # return game_information(data)
