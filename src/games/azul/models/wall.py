from dataclasses import dataclass

from src.games.azul.models import Tile


@dataclass()
class Wall:
    tiles: list[list[str]]

    @classmethod
    def new(cls) -> 'Wall':
        """Создание новой пустой стены"""
        return cls(
            tiles=[
                [f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-', f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-'],
                [f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-', f'{Tile.BLACK.value}-'],
                [f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-'],
                [f'{Tile.RED.value}-', f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-'],
                [f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-', f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-']
            ]
        )

    def export(self, player: str) -> str:
        """
        :param player: one, two
        """
        wall = ','.join('.'.join(tile) for tile in self.tiles)
        return f"wall{player}:{wall}"


if __name__ == '__main__':
    ...
