from dataclasses import dataclass

from src.games.azul.models import Factory
from src.games.azul.models import Bag


COUNT_FACTORY = {
    2: 5,
    3: 7,
    4: 9,
}


@dataclass
class Factories:
    factory: list[Factory, ...]

    @classmethod
    def new(cls, bag: Bag, players: int) -> 'Factories':
        """
        Инииализация фабрик доступных на игровом поле в зависимости от кол-ва игроков.

        Parameters:
            bag: Bag - Текущий игровой мешок с тайлами
            players: imt - Кол-во игроков

        Returned:
            Созданный экземпляр класса Factories
        """
        def get_factory():
            for _ in range(COUNT_FACTORY[players]):
                yield Factory.new_factory(bag)

        return cls(factory=list(get_factory()))


if __name__ == '__main__':

    _bag = Bag.new_bag()

    fact = Factories.new(_bag, players=2)

    print(len(_bag))
    print(fact.factory)
