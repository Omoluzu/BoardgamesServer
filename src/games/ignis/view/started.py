import random


def started_configure(games_config: dict) -> dict:
    """
    Создание стартовой конфигурации для игры ИГНИС

    games_config: Данный пришедшие с сервера.
    """
    select_one = random.sample([1, 2, 3], 2)
    select_two = random.choice([1, 2, 3])

    field = [
        [
            "F" if 1 in select_one else "",
            "F" if select_two == 1 else "",
            "F" if select_two == 2 else "",
            "W" if select_two == 2 else "",
            "W" if select_two == 1 else "",
            "W" if 1 in select_one else "",
        ],
        [
            "F" if select_two == 1 else "",
            "F" if 2 in select_one else "",
            "F" if select_two == 3 else "",
            "W" if select_two == 3 else "",
            "W" if 2 in select_one else "",
            "W" if select_two == 1 else ""
        ],
        [
            "F" if select_two == 2 else "",
            "F" if select_two == 3 else "",
            "F" if 3 in select_one else "",
            "W" if 3 in select_one else "",
            "W" if select_two == 3 else "",
            "W" if select_two == 2 else ""
        ],
        [
            "W" if select_two == 2 else "",
            "W" if select_two == 3 else "",
            "W" if 3 in select_one else "",
            "F" if 3 in select_one else "",
            "F" if select_two == 3 else "",
            "F" if select_two == 2 else ""
        ],
        [
            "W" if select_two == 1 else "",
            "W" if 2 in select_one else "",
            "W" if select_two == 3 else "",
            "F" if select_two == 3 else "",
            "F" if 2 in select_one else "",
            "F" if select_two == 1 else ""
        ],
        [
            "W" if 1 in select_one else "",
            "W" if select_two == 1 else "",
            "W" if select_two == 2 else "",
            "F" if select_two == 2 else "",
            "F" if select_two == 1 else "",
            "F" if 1 in select_one else ""
        ]
    ]

    select_type = random.randint(0, 1)

    data = {
        "field": field,
        "count": "F8W8",  # F - fire, 8 - кол-во тайлов F на поле, W - water, 8 - кол-во тайлов W на поле
        "active_player": games_config['users'][random.randint(0, 1)],
        "kind": {
            "F": games_config['users'][select_type],
            "W": games_config['users'][1 - select_type],
        },
    }

    return {
        "server": "",
        "players": data,
    }


if __name__ == '__main__':
    start = started_configure(
        games_config={
            "users": ['player1', 'player2']
        }
    )

    for fields in start['players']['field']:
        print(fields)
