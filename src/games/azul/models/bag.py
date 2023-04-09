from random import randint
from typing import Generator
from dataclasses import dataclass
from src.games.azul.models import Tile


@dataclass
class Bag:
    tiles: list

    @classmethod
    def new_bag(cls):
        return cls(
            tiles=[Tile.RED.value, Tile.BLUE.value, Tile.BLACK.value, Tile.DARK_BLUE.value, Tile.YELLOW.value] * 20)

    def __len__(self):
        return len(self.tiles)

    def give_me_tile(self, count: int = 1) -> Generator[str, ...]:
        """
        Получение необходимого кол-ва тайлов из мешка

        ::param:count - Кол-во получаемых тайлов.
        ::return: - Элементы из мешка в кол-ве указанном в count
        """
        for _ in range(count):
            index = randint(0, len(self.tiles) - 1)
            yield self.tiles.pop(index)


if __name__ == '__main__':
    ...

    bag = Bag.new_bag()

    print(bag.tiles)
    print(bag.give_me_tile(count=4))
    print(len(bag))
