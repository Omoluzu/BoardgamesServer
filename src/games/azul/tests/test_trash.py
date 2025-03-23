import pytest

from src.games.azul.view import Azul
from src.games.azul.models import (
    Factories, Pattern, Table, Floor, Box, Active,
    FirstPlayer, Bag, Wall, Count
)


"""
;
wallone:g+.y-.r-.d-.b-,b-.g-.y-.r+.d-,d+.b-.g-.y-.r-,r-.d+.b-.g-.y-,y-.r-.d-.b-.g-;
countone:4|4;
;
;
walltwo:g-.y-.r-.d+.b-,b-.g-.y-.r+.d-,d-.b-.g-.y+.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-;
counttwo:5|5;
kind:one.Omoluzu,two.Hokage;
;
active:one;
first_player:one"""


"""
bag:rdyrbdyrbdgbdgbgyrbrdgybgbgrbdgbdyrbdgyrbdgyrgrbgrgrbgyrdbgy;
box:rdddddryy
"""




@pytest.mark.azul
def test_post_tile_trash_of_table():
    """Тестирование выкладывание плитки сразу же на линию пола если у
    игрока нет места на планшете куда он может положить эту плитку.
    Плитка берется со стола"""
    azul = Azul(
        factory=Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=Pattern.imports(pattern='patternone:d.yy.-yy.----.ggggg;'),
        patterntwo=Pattern.imports(pattern='patterntwo:-.bb.rrr.yyyy.-bbbb'),
        floorone=Floor.imports(elements='floorone:x'),
        floortwo=Floor.imports(elements='floortwo:'),
        wallone=Wall.new('one'),
        walltwo=Wall.new('two'),
        countone=Count.new('one'),
        counttwo=Count.new('two'),
        table=Table.imports(tiles='table:d'),
        box=Box.new(),
        bag=Bag.new(),
        kind='kind:one.Hokage,two.Omoluzu',
        active=Active.imports(element='active:one'),
        first_player=FirstPlayer.imports(element='first_player:one')
    )

    info = {
        'command': 'trash',
        'fact': 0,
        'color': 'd',
        'player': 'one'
    }

    post_response = azul.post_trash(info=info)
    assert post_response['table'].export() == 'table:'
    assert post_response['floorone'].export() == 'floorone:xd'

    assert post_response['command']['post_floor'] == 'player.one,tile.d'
    assert post_response['command']['clean_table'] == 'd'


# TODO: Тестирование если разбито одновременно несколько плит
# TODO: Тестирование выставления плитки в TRASH если линия пола полностью заполнена
# TODO: Тестирование выставления плитки в TRASH если линия пола частична заполнена
# TODO: Тестирование выставления плитки в TRASH при условии что она взята с фабрики
# TODO: После Trash так же может наступить конец хода
# TODO: После Trash так же может наступит конец игры