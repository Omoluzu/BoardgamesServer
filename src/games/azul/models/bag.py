from random import randint
from dataclasses import dataclass

from src.games.azul.models import Tile


@dataclass
class Bag:
    tiles: list

    @classmethod
    def new_bag(cls) -> 'Bag':
        """Инициализация новой мешка по умолчанию"""
        return cls(
            tiles=[Tile.RED.value, Tile.BLUE.value, Tile.BLACK.value, Tile.DARK_BLUE.value, Tile.YELLOW.value] * 20)

    @classmethod
    def upload(cls, tiles: str) -> 'Bag':
        """
        Загрузго мешка из Экспортированного мешка

        Parameters:
            tiles (str) - строковое представление содержимого мешка.
                Где каждый символ строки это отдельный элемент в мешке
                Пример:
                    bag:rbdgyrdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbgyrbgyrbdgyrbdgyrbdy
        """
        assert tiles.startswith('bag:')
        return cls(tiles=list(tiles[4:]))

    def __len__(self):
        return len(self.tiles)

    def export(self) -> str:
        """
        Экспорт содержимого мешка

        Returned:
            bag:rbdgyrdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbdgyrbgyrbgyrbdgyrbdgyrbdy
        """
        return f"bag:{''.join(self.tiles)}"

    def give_me_tile(self, count: int = 1) -> list:
        """
        Получение необходимого кол-ва тайлов из мешка

        ::param:count - Кол-во получаемых тайлов.
        ::return: - Элементы из мешка в кол-ве указанном в count
        """
        def get_tile():
            for _ in range(count):
                index = randint(0, len(self.tiles) - 1)
                yield self.tiles.pop(index)

        return list(get_tile())


if __name__ == '__main__':
    ...
