from dataclasses import dataclass

from src.games.azul.models import Bag


@dataclass
class Factory:
    tiles: list

    def __bool__(self) -> bool:
        """Проверка наличия плиток на фабрике"""
        # print(self.tiles != ['-'])
        return self.tiles != ['-']

    @classmethod
    def new(cls, bag: Bag) -> 'Factory':
        """Инициализация новой фабрики.

        Args:
            bag:
                Текущий мешок для получения плиток

        Returns:
            Экземпляр класса Factory
        """
        return cls(tiles=bag.give_me_tile(count=4))

    @classmethod
    def imports(cls, fact: str) -> 'Factory':
        """Импортирование текущеё фабрики.

        Parameter:
            fact:
                Текущее состоянии фабрики
                yrdr

        Returned:
            Экземпляр класса Factory
        """
        return cls(tiles=list(fact))

    def export(self) -> str:
        """
        Экспорт содержимого фабрики

        Returned:
            ygbr
        """
        return ''.join(self.tiles)

    def count_tile(self, tile: str) -> int:
        """Получение кол-ва необходимого тайла на фабрике

        Args:
            tile:
                Наименование необходимого тайла
                'r'

        Returns:
            Количество искомого тайла
        """
        return self.tiles.count(tile)

    def get_other_tile(self, tile: str) -> str:
        """Получение плиток фабрики за исключение указанного

        Args:
            tile:
                Наименование необходимого тайла
                'r'

        Returns:
            'yd'
        """
        return ''.join(filter(
            lambda t: t != tile,
            self.tiles
        ))

    def action_get_tile(self, tile: str) -> dict:
        """Действие игрока на взятия плитки определенного цвета с
        текущей фабрики

        Args:
            tile:
                Цвет плитки, которую игрок хочет взять к себе на планшет
                'r'

        Returned:
            Возвращается словарь с информацией о:
                add_desc: Информация о плитках которые добавляются на стол
                count: Кол-ва взятых плиток с текущей фабрики.
        """
        data = {
            'add_desc': self.get_other_tile(tile=tile),
            'count': self.count_tile(tile=tile)
        }

        self.tiles = ['-']

        return data


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

    fact = Factory.imports('-')
    print(bool(fact))

