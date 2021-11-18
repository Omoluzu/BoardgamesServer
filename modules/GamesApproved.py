# -*- coding: utf-8 -*-

"""
Запрос на подтверждение создание игры
"""

import csv

from modules.ORM.ListGames import ListGames


def approved_games(data):

    # print(data['info_game'])
    # print(data['game_id'])

    path_games = ListGames.get_path_games(id_games=data['game_id'])
    # print(path_games)

    create_data_games = [
        ["ID", "INFO GAMES"],
        [1, data['info_game']]
    ]

    with open(path_games, 'w') as f:
        writer = csv.writer(f)
        for row in create_data_games:
            writer.writerow(row)

    message_chat = {
        "command": "message",
        "message": f"{path_games}",
        "user": "System"
    }

    return message_chat
