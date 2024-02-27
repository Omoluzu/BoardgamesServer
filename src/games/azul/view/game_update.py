from modules.GameInformation import game_information


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


def game_update(data: dict) -> dict:
    print('game_update', data)
    game_command = split_game_command(data.get('game_command'))

    game = game_information(data)

    print('game', game)
    print('game_command', game_command)

    match game_command['command']:
        case 'post':
            from src.games.azul.commands import post
            ...


    return data


