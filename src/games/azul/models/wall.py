from dataclasses import dataclass

from src.games.azul.models import Tile


@dataclass()
class Wall:
    player: str
    tiles: list[list[str]]

    @classmethod
    def new(cls, player: str) -> 'Wall':
        """Создание новой пустой стены"""
        return cls(
            player=player,
            tiles=[
                [f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-', f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-'],
                [f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-', f'{Tile.BLACK.value}-'],
                [f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-'],
                [f'{Tile.RED.value}-', f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-', f'{Tile.YELLOW.value}-'],
                [f'{Tile.YELLOW.value}-', f'{Tile.RED.value}-', f'{Tile.BLACK.value}-', f'{Tile.BLUE.value}-', f'{Tile.DARK_BLUE.value}-']
            ]
        )

    @classmethod
    def imports(cls, elements: str) -> 'Wall':
        """
        :param elements: wallone:g-.y-.r-.d-.b-,b-.g-.y-.r-.d-,d-.b-.g-.y-.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-
        """
        name, _element = elements.split(':')

        return cls(
            player=name[4:],
            tiles=list(element.split('.') for element in _element.split(','))
        )

    def export(self) -> str:
        """
        :param player: one, two
        """
        wall = ','.join('.'.join(tile) for tile in self.tiles)
        return f"wall{self.player}:{wall}"


if __name__ == '__main__':
    wall = Wall.imports(elements='wallone:g-.y-.r-.d-.b-,b-.g-.y-.r-.d-,d-.b-.g-.y-.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-')
    print(wall.export())