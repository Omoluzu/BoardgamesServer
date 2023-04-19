import random


def started_configure(games_config: dict) -> dict:
    """
    Создание стартовой конфигурации для игры ИГНИС

    games_config: Данный пришедшие с сервера.
    """
    field = [
        ["F", "F", "", "", "W", "W"],
        ["F", "", "", "", "", "W"],
        ["", "", "F", "W", "", ""],
        ["", "", "W", "F", "", ""],
        ["W", "", "", "", "", "F"],
        ["W", "W", "", "", "F", "F"]
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
