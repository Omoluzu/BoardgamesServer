from src.games.azul.models import Bag, Factories


def started_configure(data: dict):
    """
    Создание стартовой конфигурации для игры AZUL

    data: Данный пришедшие с сервера.
    """
    bag = Bag.new()
    factories = Factories.new(bag=bag, players=data.get('players'))

    print(factories.export())


if __name__ == '__main__':
    started_configure({
        'players': 2
    })

