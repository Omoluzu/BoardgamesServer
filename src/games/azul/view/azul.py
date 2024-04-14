"""
АЗУЛ
Взаимодействие клиента с сервером
"""
import re

from dataclasses import dataclass

from src.games.azul.models import Factories, Pattern, Table, Floor, Tile


REGULAR = (
    r'(?P<fact>fact:[^;]*);'
    r'(?P<patternone>patternone:[^;]*);'
    r'(?P<floorone>floorone:[^;]*);'
    r'(?P<floortwo>floortwo:[^;]*);'
    r'(?P<patterntwo>patterntwo:[^;]*);'
    r'(?P<kind>kind:[^;]*);'
    r'(?P<table>table:[^;]*)'
)


@dataclass
class Azul:
    factory: Factories  # Фабрики
    patternone: Pattern  # Планшет игрока номер 1
    patterntwo: Pattern  # Планшет игрока номер 2
    floorone: Floor  # Линия пола игрока 1
    floortwo: Floor  # Линия пола игрока 2
    table: Table  # Игровой стол

    @classmethod
    def open_save(cls, game_id, test=False) -> 'Azul':
        """Открытие игровой сессии из базы данных

        Args:
            game_id: ИД игры
            test: Тестирование игры
        """
        from modules.GameInformation import game_information

        game = game_information(data={'game_id': game_id}, test=test)
        match_game_info = re.match(REGULAR, game['game_info'])

        return cls(
            factory=Factories.imports(match_game_info.group('fact')),
            patternone=Pattern.imports(match_game_info.group('patternone')),
            patterntwo=Pattern.imports(match_game_info.group('patterntwo')),
            floorone=Floor.imports(match_game_info.group('floorone')),
            floortwo=Floor.imports(match_game_info.group('floortwo')),
            table=Table.imports(match_game_info.group('table'))
        )

    def post(self, info: dict) -> dict:
        """Выставление плитки на планшет игрока

        Args:
            info: Информация пришедшая с клиента

        Returns:
            Ответ на его действия
        """
        if info['fact']:
            data = self.factory.get_tile(
                factory_number=int(info['fact']),
                tile=info['color']
            )
            self.table.put(tiles=data['add_desc'])
            data['clean_fact'] = info['fact']
        else:
            data = self.table.get_tile(color=info['color'])

        pattern = getattr(self, f"pattern{info['player']}")
        pattern.post_tile(
            line=info['line'],
            tiles=info['color'] * data['count']
        )

        floor = getattr(self, f"floor{info['player']}")
        post_floor_tile = ''

        if Tile.FIRST_PLAYER.value in data.get('clean_table', ''):
            floor.element_add(element=Tile.FIRST_PLAYER.value)
            post_floor_tile += Tile.FIRST_PLAYER.value

        if excess_tile := pattern.excess_tile > 0:
            elements=info['color'] * excess_tile
            floor.element_add(element=elements)
            post_floor_tile += elements

        if post_floor_tile:
            data['post_floor'] = f"player.{info['player']},tile.{post_floor_tile}"


        return {

            'fact': self.factory,
            'patternone': self.patternone,
            'patterntwo': self.patterntwo,
            'floorone': self.floorone,
            'floortwo': self.floortwo,
            'table': self.table,
            'command': {
                'post_pattern_line': f"line.{info['line']},player.{info['player']},tile.{info['color']},count.{data['count']}",
                **data
            }
        }
