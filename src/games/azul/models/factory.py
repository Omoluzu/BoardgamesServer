from dataclasses import dataclass

from src.games.azul.models import Bag


@dataclass
class Factory:
    tiles: list

    @classmethod
    def new(cls, bag: Bag) -> 'Factory':
        """
        Инициализация новой фабрики.

        Parameter:
            bag: Текущий мешок для получения тайлов

        Returned:
            Экземпляр класса Factory
        """
        return cls(tiles=bag.give_me_tile(count=4))

    def export(self) -> str:
        """
        Экспорт содерживого фабрики

        Returned:
            ygbr
        """
        return ''.join(self.tiles)


if __name__ == '__main__':

    bag_ = Bag.new()

    factory = Factory.new(bag_)
    print(factory.tiles)
    factory1 = Factory.new(bag_)
    print(factory1.tiles)
    factory2 = Factory.new(bag_)
    print(factory2.tiles)
    factory3 = Factory.new(bag_)
    print(factory3.tiles)

    print(len(bag_))

