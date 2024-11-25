from dataclasses import dataclass
from typing import Iterable

from src.games.azul.models import Factory, Bag


COUNT_FACTORY = {
    2: 5,
    3: 7,
    4: 9,
}


@dataclass
class Factories:
    factory: list[Factory, ...]

    def __bool__(self) -> bool:
        """Проверка наличия плиток на фабриках"""
        for factory in self.factory:
            if factory:
                return True

        return False

    @classmethod
    def new(cls, bag: Bag, players: int) -> 'Factories':
        """Инициализация фабрик доступных на игровом поле
        в зависимости от кол-ва игроков.

        Args:
            bag:
                Bag - Текущий игровой мешок с плитками
            players:
                int - Кол-во игроков

        Returns:
            Созданный экземпляр класса Factories
        """
        def get_factory():
            for _ in range(COUNT_FACTORY[players]):
                yield Factory.new(bag)

        return cls(factory=list(get_factory()))

    @classmethod
    def imports(cls, fact: str) -> 'Factories':
        """Импортирование текущего состояния фабрик.

        Args:
            fact:
                Текущие содержание фабрик
                fact:rgyd.rygd.dggb.bygb.yrdr

        Returns:
            Созданный экземпляр класса Factories
        """
        assert fact.startswith('fact:')

        factory = map(
            lambda tiles: Factory.imports(tiles),
            fact[5:].split('.')
        )

        return cls(factory=list(factory))

    def export(self) -> str:
        """
        Экспорт содержимого фабрик игрового поля.

        Returns:
            fac:ygbr.rbdd.rydy.rrrr.dbgr
        """
        def export_factory():
            for factory in self.factory:
                yield factory.export()

        return f"fact:{'.'.join(export_factory())}"

    def get_tile(self, factory_number: int, tile: str) -> dict:
        """Взятие плиток с фабрики

        Args:
            factory_number: Номер фабрики с которой нужно взять плитки.
            tile: цвет тайла который необходимо взять с фабрики.
                'r'

        Returns:
            Информация о взятии
        """
        factory = self.factory[factory_number - 1]
        return factory.action_get_tile(tile=tile)

    def post_tile(self, bag: Bag) -> Iterable[str]:
        """Заполнение фабрик плитками из мешка

        Args:
            bag:
                Экземпляр класса мешка. Для взятия плиток

        Returns:
            Генератор содержащий информацию о выставленных плитках
        """
        for factory in self.factory:
            tiles = bag.give_me_tile(count=4)
            factory.post_tile(tiles=tiles)
            yield ''.join(tiles)


if __name__ == '__main__':

    _bag = Bag.new()

    fact = Factories.new(_bag, players=2)

    print(len(_bag))
    print(fact.export())

    """
    fac:1234.__34.12_4.12__.1234
    
    """
