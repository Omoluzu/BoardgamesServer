"""Тестирование выставление найлов на стену и подсчет очков"""

import pytest

from src.games.azul import models, view


@pytest.mark.azul
def test_post_wall_command_post_wall():
    """Тестирование команды на выставление плиток на стену игрока"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floorone:x'),
        wallone=models.Wall.new('one'),
        walltwo=models.Wall.new('two'),
        table=models.Table.imports(tiles='table:y'),
        box=models.Box.new(),
        bag=models.Bag.new(),
        kind='kind:one.Hokage,two.Omoluzu',
        active=models.Active.imports(element='active:one'),
        first_player=models.FirstPlayer.imports(element='first_player:two')
    )

    info = {
        'command': 'post',
        'fact': 0,
        'color': 'y',
        'line': 5,
        'player': 'one'
    }

    post_response = azul.post(info=info)
    assert post_response['command']['post_wall'] == 'one.grdd-,two.dry--'
    assert post_response['wallone'].export() == 'wallone:g+.y-.r-.d-.b-,b-.g-.y-.r+.d-,d+.b-.g-.y-.r-,r-.d+.b-.g-.y-,y-.r-.d-.b-.g-'
    assert post_response['walltwo'].export() == 'walltwo:g-.y-.r-.d+.b-,b-.g-.y-.r+.d-,d-.b-.g-.y+.r-,r-.d-.b-.g-.y-,y-.r-.d-.b-.g-'



@pytest.mark.azul
def test_post_clean_pattern():
    """тестирование очистки pattern"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floorone:x'),
        wallone=models.Wall.new('one'),
        walltwo=models.Wall.new('two'),
        table=models.Table.imports(tiles='table:y'),
        box=models.Box.new(),
        bag=models.Bag.new(),
        kind='kind:one.Hokage,two.Omoluzu',
        active=models.Active.imports(element='active:one'),
        first_player=models.FirstPlayer.imports(element='first_player:two')
    )

    info = {
        'command': 'post',
        'fact': 0,
        'color': 'y',
        'line': 5,
        'player': 'one'
    }

    post_response = azul.post(info=info)
    assert post_response['patternone'].export() == 'patternone:-.--.---.----.----y'
    assert post_response['patterntwo'].export() == 'patterntwo:-.--.---.---g.---bb'



# todo выставление новых плиток на фабрику
# todo Жетон первого игрока на столе
# todo Очистка линии пола
# todo Уменьшение содержимого мешка
# todo Увеличение содержимое коробки
# todo Ходит тот игрок у кого был жетон первого игрока (Не важно кто последний сделал ход)
# todo Подсчет и сохранение кол-ва победных очков
