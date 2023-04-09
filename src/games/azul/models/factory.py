from dataclasses import dataclass

from src.games.azul.models import Bag


@dataclass
class Factory:
    tiles: list

    @classmethod
    def new_factory(cls, bag: Bag) -> 'Factory':
        """
        Инициализация новой фабрики.

        Parameter:
            bag: Текущий мешок для получения тайлов

        Returned:
            Экземпляр класса Factory
        """
        return cls(tiles=bag.give_me_tile(count=4))


if __name__ == '__main__':

    bag_ = Bag.new_bag()

    factory = Factory.new_factory(bag_)
    print(factory.tiles)
    factory1 = Factory.new_factory(bag_)
    print(factory1.tiles)
    factory2 = Factory.new_factory(bag_)
    print(factory2.tiles)
    factory3 = Factory.new_factory(bag_)
    print(factory3.tiles)

    print(len(bag_))

