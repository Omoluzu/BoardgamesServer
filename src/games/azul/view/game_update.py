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


def zip_game_command(info: dict) -> str:
    """
    {'command': 'post', 'fact': 5, 'color': 'r', 'line': 3}
    ->
    'command:post;fact:5;color:r;line:3'
    """
    data = ''
    for key, value in info.items():
        data += f'{key}:{value};'
    return data[:-1]


def update_azul(data: dict, test=False) -> dict:
    game_command = split_game_command(data.get('game_command'))

    azul = Azul.open_save(game_id=data['game_id'], test=test)

    match game_command['command']:
        case 'post':
            response = azul.post(game_command)
        case _:
            response = {}

    data['game_command'] = zip_game_command(response.get('command'))
    return data
