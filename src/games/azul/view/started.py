from src.games.azul.models import Bag, Factories


def started_configure(games_config: dict):
    """
    Создание стартовой конфигурации для игры AZUL

    games_config: Данный пришедшие с сервера.
    """
    bag = Bag.new()
    factories = Factories.new(bag=bag, players=games_config.get('select_players'))

    return factories.export()


if __name__ == '__main__':
    started_configure({
        'select_players': 2
    })

