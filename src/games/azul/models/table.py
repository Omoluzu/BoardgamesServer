"""Описание логики игры с игровым столом"""
from dataclasses import dataclass

from src.games.azul.models import Tile


@dataclass
class Table:
    """Игровой стол

    Attributes:
        tiles: Плитки расположенные на игровом столе
    """
    tiles: list[str, ...]

    @classmethod
    def imports(cls, tiles: str) -> 'Table':
        """Импорт состояния игрового стала

        Args:
            tiles: Информация о плитках на игровом столе
                xggbb

        Return:
            Инициализированный класс игрового стола игры
        """
        return cls(tiles=list(tiles.replace('table:', '')))

    def put(self, tiles: str):
        """Выложить плитки на стол

        Args:
            tiles: Список плиток которые необходимо выложить на стол
                'rb'
        """
        self.tiles.extend(list(tiles))

    def remove(self, color: str) -> None:
        """Удаление плиток с игрового стола

        Args:
            color: Цвет плитки необходимый для удаления
        """
        for _ in range(self.tiles.count(color)):
            self.tiles.remove(color)

    def get_tile(self, color: str) -> dict:
        """Взятие тайла со стола

        Args:
            color: Цвет плитки необходимый для взятия

        Returns:
            Словарик с информацией о взятых плитках
                count: кол-во взятых плиток со стола
                clean_table: Плитки которые необходимо удалит со стола
                    'xb'
        """
        count = self.tiles.count(color)
        self.remove(color)
        clean_table = color

        if Tile.FIRST_PLAYER.value in self.tiles:
            self.tiles.remove(Tile.FIRST_PLAYER.value)
            clean_table = ''.join([Tile.FIRST_PLAYER.value, color])

        return {
            'count': count,
            'clean_table': clean_table
        }

    def export(self):
        """Экспортирование содержимое игрового стола

        Returns:
            Плитки на игровом столе
        """
        return f"table:{''.join(self.tiles)}"
