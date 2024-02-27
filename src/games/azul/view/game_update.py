import re

from modules.GameInformation import game_information
from src.games.azul.models import Factories

R = r'(?P<fact>fact:[^;]*)'


def split_game_command(info: str) -> dict:
    """
    'command:post;fact:5;color:r;line:3'
    ->
    {'command': 'post', 'fact': 5, 'color': 'r', 'line': 3}

    """
    data = {}
    for i in info.split(';'):
        x = i.split(':')
        data[x[0]] = int(x[1]) if x[1].isdigit() else x[1]
    return data


def update_azul(data: dict, test=False) -> dict:
    print('game_update', data)
    game_command = split_game_command(data.get('game_command'))

    game = game_information(data, test=test)
    match_game_info = re.match(R, game['game_info'])

    factory = Factories.imports(match_game_info.group('fact'))

    print('game', game)
    print('game_command', game_command)

    match game_command['command']:
        case 'post':
            from src.games.azul.commands import post
            ...

    return data


if __name__ == '__main__':
    info = {
        'test': True,
        'command': 'game_update',
        'user': 'Omoluzu',
        'games': 'azul',
        'game_id': 1,
        'game_command': 'command:post;fact:3;color:g;line:2'
    }

    update_azul(info, test=True)
