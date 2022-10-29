
"""
Запрос на обновление игры
"""
import os
import csv
import json

from modules.ORM.ListGames import ListGames
from modules.GameInformation import game_information
from modules.Game.IGNIS import destroy_field, expose_unit, get_count_unit, change_active_player


def update_ignis(data: dict):
    """ Обновление информации по игре Игнис """
    match data['game_command']['command']:
        case 'expose_unit':

            game = game_information(data)
            data_expose = expose_unit(game['game_info']['field'], **data['game_command'])
            data_destroy = destroy_field(data_expose['field'])
            count = get_count_unit(data_destroy['field'])
            new_active_player = change_active_player(
                current_active_player=game['game_info']['active_player'], users=game['game_info']['kind']
            )

            data['game_info'] = {
                "field": data_destroy['field'],
                "count": count['count'],
                "active_player": new_active_player,
                "kind": game['game_info']['kind']
            }
            data['game_command'] = {
                "move": data_expose['move'],
                "destroy": data_destroy['destroy'],
                "count": count['count'],
                "active_player": new_active_player
            }

    return data


def game_update(data: dict):

    match data.get('games'):
        case 'ignis':
            data = update_ignis(data)

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
        'user': data.get('user', None),
        'game_id': data['game_id'],
        # 'game_info': data['game_info'],
        'game_command': data['game_command'],
    }
