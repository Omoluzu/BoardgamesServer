import random

from copy import copy

from src.games.azul.models import Bag, Factories


def started_configure(games_config: dict) -> dict:
    """
    Создание стартовой конфигурации для игры AZUL

    games_config: Данный пришедшие с сервера.
    """
    bag = Bag.new()
    factories = Factories.new(bag=bag, players=games_config['games_config']['select_players'])

    user = copy(games_config['users'])
    one = user.pop(random.randint(0, 1))
    two = user[0]
    kind = f'kind:one.{one},two.{two}'

    return {
        "server": bag.export(),
        "players": f"{factories.export()};patternone:-.--.---.----.-----;patterntwo:-.--.---.----.----;{kind}"
    }


if __name__ == '__main__':
    info = started_configure({
        'create_user': 'Omoluzu',
        'games_config': {
            'select_players': 2,
            'select_unit': 'random'
        },
        'games': 'azul',
        'users': ['Omoluzu', 'Hokage']}
)


