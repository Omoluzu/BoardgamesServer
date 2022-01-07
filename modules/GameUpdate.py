
"""
Запрос на обновление игры
"""


def game_update(data: dict):

    return {
        'command': 'game_update',
        'game_id': data['game_id'],
        'game_command': data['game_command'],
    }
