import random

from copy import copy

from src.games.azul.models import Bag, Factories, Wall


def started_configure(games_config: dict) -> dict:
    """Создание стартовой конфигурации для игры AZUL

    :param games_config: Данный пришедшие с сервера.
    """

    wall = Wall.new()
    bag = Bag.new()
    factories = Factories.new(bag=bag, players=games_config['games_config']['select_players'])

    user = copy(games_config['users'])
    one = user.pop(random.randint(0, 1))
    two = user[0]
    kind = f'kind:one.{one},two.{two}'

    return {
        "server": f"{bag.export()};box:",
        "players": f"{factories.export()};patternone:-.--.---.----.-----;floorone:;wallone:{wall.export('one')};patterntwo:-.--.---.----.-----;floortwo:;walltwo:{wall.export('two')};{kind};table:x;active:one;first_player:one"
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


