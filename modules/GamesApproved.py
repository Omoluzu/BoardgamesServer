# -*- coding: utf-8 -*-

"""
Запрос на подтверждение создание игры
"""

import os
import csv
import json

from modules.ORM.ListGames import ListGames
from modules.GameInformation import game_information


def approved_games(data):

    path = ListGames.get_path_games(id_games=data['game_id'])

    if not os.path.exists(path):
        os.mkdir(path)

    path_games = os.path.join(path, f"{str(data['game_id'])}.csv")

    create_data_games = [
        ["ID", "INFO GAMES"],
        [1, json.dumps(data['info_game'])]
    ]

    with open(path_games, 'w') as f:
        writer = csv.writer(f)
        for row in create_data_games:
            writer.writerow(row)

    return game_information(data)
