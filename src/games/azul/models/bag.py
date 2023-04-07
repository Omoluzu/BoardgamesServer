from dataclasses import dataclass
from src.games.azul.models import Tile


@dataclass
class Bag:
    tiles: list[Tile, ...]

    @classmethod
    def new_bag(cls):
        return cls(tiles=[Tile.RED, Tile.BLUE, Tile.BLACK, Tile.DARK_BLUE, Tile.YELLOW] * 20)


if __name__ == '__main__':
    ...
    # bug = [Tile.RED, Tile.BLUE, Tile.BLACK, Tile.DARK_BLUE, Tile.YELLOW] * 20
    # print(bug)

    bag = Bag.new_bag()

    print(bag.tiles)
