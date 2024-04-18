"""
АЗУЛ
Взаимодействие клиента с сервером
"""
import re

from dataclasses import dataclass

from src.games.azul import models


REGULAR = (
    r'(?P<fact>fact:[^;]*);'
    r'(?P<patternone>patternone:[^;]*);'
    r'(?P<floorone>floorone:[^;]*);'
    r'(?P<floortwo>floortwo:[^;]*);'
    r'(?P<patterntwo>patterntwo:[^;]*);'
    r'(?P<kind>kind:[^;]*);'
    r'(?P<table>table:[^;]*)'
)

SERVER_REGULAR = (
    r'(?P<bag>bag:[^;]*);'
    r'(?P<box>box:[^;]*);'
)


@dataclass
class Azul:
    factory: models.Factories  # Фабрики
    patternone: models.Pattern  # Планшет игрока номер 1
    patterntwo: models.Pattern  # Планшет игрока номер 2
    floorone: models.Floor  # Линия пола игрока 1
    floortwo: models.Floor  # Линия пола игрока 2
    table: models.Table  # Игровой стол
    box: models.Box  # Содержимое игровой коробки (Сбрасываются лишние игровые плитки)

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
        match_server_info = re.match(SERVER_REGULAR, game['server_info'])

        return cls(
            factory=models.Factories.imports(match_game_info.group('fact')),
            patternone=models.Pattern.imports(match_game_info.group('patternone')),
            patterntwo=models.Pattern.imports(match_game_info.group('patterntwo')),
            floorone=models.Floor.imports(match_game_info.group('floorone')),
            floortwo=models.Floor.imports(match_game_info.group('floortwo')),
            table=models.Table.imports(match_game_info.group('table')),
            box=models.Box.imports(match_server_info.group('box'))
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

        if models.Tile.FIRST_PLAYER.value in data.get('clean_table', ''):
            floor.element_add(element=models.Tile.FIRST_PLAYER.value)

        floor.element_add(element=info['color'] * pattern.excess_tile)
        self.box.element_add(element=floor.log.element_extra)

        if floor.log.element_add:
            data['post_floor'] = f"player.{info['player']},tile.{''.join(floor.log.element_add)}"

        return {
            'fact': self.factory,
            'patternone': self.patternone,
            'patterntwo': self.patterntwo,
            'floorone': self.floorone,
            'floortwo': self.floortwo,
            'table': self.table,
            'box': self.box,
            'command': {
                'post_pattern_line': f"line.{info['line']},player.{info['player']},tile.{info['color']},count.{pattern.put_tile}",
                **data
            }
        }
