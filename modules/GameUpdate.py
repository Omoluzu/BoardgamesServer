
"""
Запрос на обновление игры
"""
import os
import csv
import json

from modules.ORM.ListGames import ListGames


def game_update(data: dict):

    if not data.get('test'):

        path_games = ListGames.get_path_games(id_games=data['game_id'])

        if os.path.isfile(path_games):
            with open(path_games) as f:
                reader = csv.reader(f)
                game_info = list(reader)[-2]

        with open(path_games, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([
                int(game_info[0]) + 1,
                json.dumps(data['game_info'])
            ])

    return {
        'command': 'game_update',
        'game_id': data['game_id'],
        'game_command': data['game_command'],
    }
