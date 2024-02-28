from src.games.azul.view.azul import Azul


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

    game = Azul.open_save(game_id=data['game_id'], test=test)

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
