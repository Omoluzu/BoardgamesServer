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
    r'(?P<wallone>wallone:[^;]*);'
    r'(?P<countone>countone:[^;]*);'
    r'(?P<patterntwo>patterntwo:[^;]*);'
    r'(?P<floortwo>floortwo:[^;]*);'
    r'(?P<walltwo>walltwo:[^;]*);'
    r'(?P<counttwo>counttwo:[^;]*);'
    r'(?P<kind>kind:[^;]*);'
    r'(?P<table>table:[^;]*);'
    r'(?P<active>active:[^;]*);'
    r'(?P<first_player>first_player:[^;]*)'
)

SERVER_REGULAR = (
    r'(?P<bag>bag:[^;]*);'
    r'(?P<box>box:[^;]*)'
)

NEGATIVE_COUNT_FLOOR = {
    0: 0,
    1: -1,
    2: -2,
    3: -4,
    4: -6,
    5: -8,
    6: -11,
    7: -14
}


@dataclass
class Azul:
    factory: models.Factories  # Фабрики
    patternone: models.Pattern  # Планшет игрока номер 1
    patterntwo: models.Pattern  # Планшет игрока номер 2
    floorone: models.Floor  # Линия пола игрока 1
    floortwo: models.Floor  # Линия пола игрока 2
    wallone: models.Wall  # Стена игрока 1
    walltwo: models.Wall  # Стена игрока 2
    countone: models.Count  # Стена игрока 2
    counttwo: models.Count  # Стена игрока 2
    table: models.Table  # Игровой стол
    box: models.Box  # Содержимое игровой коробки (Сбрасываются лишние игровые плитки)
    bag: models.Bag  # Сумка с плитками игрока.
    active: models.Active  # Активный игрок
    first_player: models.FirstPlayer  # Первый игрок
    kind: str  # Порядок хода игроков

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
            wallone=models.Wall.imports(match_game_info.group('wallone')),
            walltwo=models.Wall.imports(match_game_info.group('walltwo')),
            countone=models.Count.imports(match_game_info.group('countone')),
            counttwo=models.Count.imports(match_game_info.group('counttwo')),
            table=models.Table.imports(match_game_info.group('table')),
            active=models.Active.imports(match_game_info.group('active')),
            first_player=models.FirstPlayer.imports(match_game_info.group('first_player')),
            kind=match_game_info.group('kind'),
            box=models.Box.imports(match_server_info.group('box')),
            bag=models.Bag.upload(match_server_info.group('bag')),
        )

    def save(self) -> dict:
        """Сбор информации о всех ключевых элементах игры"""
        return {
            'fact': self.factory,
            'patternone': self.patternone,
            'patterntwo': self.patterntwo,
            'floorone': self.floorone,
            'floortwo': self.floortwo,
            'wallone': self.wallone,
            'walltwo': self.walltwo,
            'countone': self.countone,
            'counttwo': self.counttwo,
            'table': self.table,
            'box': self.box,
            'bag': self.bag,
            'active': self.active,
            'first_player': self.first_player,
            'kind': self.kind,
        }


    def post_trash(self, info: dict) -> dict:
        """Выставление плиток на линию пола, миную планшет игрока.
            Происходит когда игрок не может выставить плитку на свой планшет

        Args:
            info: Информация пришедшая с клиента

        Returns:
            Ответ на его действия
        """
        data = {}

        count_tile_table = self.table.tiles.count(info['color'])
        self.table.remove(info['color'])

        floor = getattr(self, f"floor{info['player']}")
        floor.element_add(element=info['color'] * count_tile_table)

        if not self.table and not self.factory:
            data.update(self.post_wall())

        return {
            **self.save(),
            'command': {
                'post_floor': f"player.{info['player']},tile.{info['color']}",
                'clean_table': info['color'] * count_tile_table,
                **data
            }
        }

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
            if models.Tile.FIRST_PLAYER.value in list(data['clean_table']):
                self.first_player.change_first_player(info['player'])
                data['change_first_player'] = info['player']

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

        if not self.table and not self.factory:
            data.update(self.post_wall())

        self.active.change_player()

        return {
            **self.save(),
            'command': {
                'post_pattern_line': f"line.{info['line']},player.{info['player']},tile.{info['color']},count.{pattern.put_tile}",
                'active_player': self.active.element,
                **data
            }
        }

    def post_wall(self) -> dict[str, str]:
        """Команда на выставление плиток на линию пола

        Returns:
            Информация для передачи клиентскому приложению
        """
        playerone = self.patternone.post_wall()
        playertwo = self.patterntwo.post_wall()

        countone = self.wallone.post_wall(playerone)
        countone += NEGATIVE_COUNT_FLOOR[len(self.floorone)]

        counttwo = self.walltwo.post_wall(playertwo)
        counttwo += NEGATIVE_COUNT_FLOOR[len(self.floortwo)]

        self.countone.update(value=countone)
        self.counttwo.update(value=counttwo)

        self.table.put(tiles=models.Tile.FIRST_PLAYER.value)

        post_tiles = self.factory.post_tile(bag=self.bag)

        if models.Tile.FIRST_PLAYER.value in self.floorone.elements:
            self.first_player.change_first_player(value='one')
        elif models.Tile.FIRST_PLAYER.value in self.floortwo.elements:
            self.first_player.change_first_player(value='two')

        self.floorone.clear()
        self.floortwo.clear()
        self.box.add_element_before_post_wall(
            element_player_one=playerone, element_player_two=playertwo)

        return {
            'post_wall': f'one.{"".join(playerone)},two.{"".join(playertwo)}',
            'post_fact': '.'.join(post_tiles),
            'add_desc': models.Tile.FIRST_PLAYER.value,
            'floor_clear': '+',
            'change_first_player': self.first_player.element,
            'change_count': f'one.{self.countone.element},two.{self.counttwo.element}'
        }
