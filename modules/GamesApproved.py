# -*- coding: utf-8 -*-

"""
Запрос на подтверждение создание игры
"""

import csv
import json

from modules.ORM.ListGames import ListGames
from modules.GameInformation import game_information


def approved_games(data):

    path_games = ListGames.get_path_games(id_games=data['game_id'])

    create_data_games = [
        ["ID", "INFO GAMES"],
        [1, json.dumps(data['info_game'])]
    ]

    with open(path_games, 'w') as f:
        writer = csv.writer(f)
        for row in create_data_games:
            writer.writerow(row)

    return game_information(data)
