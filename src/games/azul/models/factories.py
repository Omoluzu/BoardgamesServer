from dataclasses import dataclass

from src.games.azul.models import Factory, Bag


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
            players: int - Кол-во игроков

        Returned:
            Созданный экземпляр класса Factories
        """
        def get_factory():
            for _ in range(COUNT_FACTORY[players]):
                yield Factory.new(bag)

        return cls(factory=list(get_factory()))

    def export(self) -> str:
        """
        Экспорт содержимого фабрик игрового поля.

        Returned:
            fac:ygbr.rbdd.rydy.rrrr.dbgr
        """
        def export_factory():
            for factory in self.factory:
                yield factory.export()

        return f"fac:{'.'.join(export_factory())}"


if __name__ == '__main__':

    _bag = Bag.new()

    fact = Factories.new(_bag, players=2)

    print(len(_bag))
    print(fact.export())

    """
    fac:1234.__34.12_4.12__.1234
    
    """
