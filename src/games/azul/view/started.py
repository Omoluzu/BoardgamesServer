from src.games.azul.models import Bag, Factories


def started_configure(data: dict):
    """
    Создание стартовой конфигурации для игры AZUL

    data: Данный пришедшие с сервера.
    """
    bag = Bag.new()
    factories = Factories.new(bag=bag, players=data.get('players'))


