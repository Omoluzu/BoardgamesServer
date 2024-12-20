from dataclasses import dataclass

from src.games.azul.models import Tile


@dataclass()
class Wall:
    player: str
    tiles: list[list[str]]

    @classmethod
    def new(cls, player: str) -> 'Wall':
        """Создание новой пустой стены

        Return:
            Экземпляр класс стены
        """
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
        """Импорт из сохраненной сессии.

        Args:
             elements: wallone:g-.y-.r-.d-.b-,b-.g-.y-.r-.d-,d-.b-.g-.y-.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-

        Return:
            Экземпляр класс стены
        """
        name, _element = elements.split(':')

        return cls(
            player=name[4:],
            tiles=list(element.split('.') for element in _element.split(','))
        )

    def post_wall(self, data: list[str]) -> int:
        """Выставление собранных плиток на линиях на стену

        Args:
            data: содержимое плиток которые должны быть выставлены на стену.
                ['g', 'r', 'd', 'd', '-']
                ['d', 'r', 'y', '-', '-']

        Return:
            Количество победных очков заработанные игроком после
                выставление плиток на стол.
        """
        count = 0

        for line, tile in enumerate(data):
            if tile != '-':
                index_position = self.tiles[line].index(f"{tile}-")
                self.tiles[line][index_position] = f'{tile}+'

                index_check_up = line
                while True:
                    index_check_up -= 1
                    try:
                        tile = self.tiles[index_check_up][index_position]
                    except IndexError:
                        break
                    else:
                        if tile[1] == "+":
                            count += 1
                        else:
                            break

                count += 1

        return count


    def export(self) -> str:
        """Экспорт данных стены

        Returns:
            Информация о текущем содержании плиток на стене.
            wallone:g-.y-.r-.d-.b-,b-.g-.y-.r-.d-,d-.b-.g-.y-.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-
        """
        wall = ','.join('.'.join(tile) for tile in self.tiles)
        return f"wall{self.player}:{wall}"


if __name__ == '__main__':
    wall = Wall.imports(elements='wallone:g-.y-.r-.d-.b-,b-.g-.y-.r-.d-,d-.b-.g-.y-.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-')
    wall.post_wall(data=['g', 'r', 'd', 'd', '-'])
    print(wall.export())