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

    def export(self):
        """Экспортирование содержимое игрового стола

        Returns:
            Плитки на игровом столе
        """
        return f"table:{''.join(self.tiles)}"
