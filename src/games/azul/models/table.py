"""Описание логики игры с игровым столом"""
from dataclasses import dataclass


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
        """
        count = self.tiles.count(color)
        self.remove(color)
        self.tiles.remove('x')

        return {
            'count': count
        }

    def export(self):
        """Экспортирование содержимое игрового стола

        Returns:
            Плитки на игровом столе
        """
        return f"table:{''.join(self.tiles)}"
