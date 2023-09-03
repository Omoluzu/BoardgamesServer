# -*- coding: utf-8 -*-

"""
Запрос на подтверждение создание игры
"""

import os
import csv
import json

from modules.ORM.ListGames import ListGames
from modules.GameInformation import game_information
from src.games import start_game


def approved_games(data):
    game_info = ListGames.get_games_info(games_id=data['game_id'])
    started_configure = start_game.get(game_info['games'])
    game_data = started_configure(games_config=game_info)

    path_games = ListGames.get_path_games(id_games=data['game_id'])

    if not os.path.exists(os.path.dirname(path_games)):
        os.mkdir(os.path.dirname(path_games))

    create_data_games = [
        ["ID", "INFO GAMES", "SERVER INFO"],
        [
            1,
            json.dumps(game_data.get('players')),
            json.dumps(game_data.get('server'))
        ],
    ]

    with open(path_games, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in create_data_games:
            writer.writerow(row)

    return {
        "command": "game_info",
        "game_id": data['game_id'],
        "games": game_info['games'],
        "game_info": game_data.get('players')  # Информация не должна быть пустой,
        # иначе идет проверка на повторный апрув создание игры
    }
    # return game_information(data)
