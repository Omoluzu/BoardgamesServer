"""Тестирование выставление найлов на стену и подсчет очков"""
import re
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
        floortwo=models.Floor.imports(elements='floortwo:x'),
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
        floortwo=models.Floor.imports(elements='floortwo:x'),
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


@pytest.mark.azul
def test_post_clean_pattern():
    """выставление новых плиток на фабрику"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floortwo:x'),
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

    post_fact_regex = re.compile(r"^((?:\w{4}\.){4}\w{4})")
    export_fact_regex = re.compile(r"^(fact:(?:\w{4}\.){4}\w{4})")

    assert post_fact_regex.match(post_response['command']['post_fact']) is not None
    assert export_fact_regex.match(post_response['fact'].export()) is not None



@pytest.mark.azul
def test_post_tile_first_player_in_table():
    """Жетон первого игрока на столе"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floortwo:x'),
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

    assert post_response['table'].export() == 'table:x'
    assert post_response['command']['add_desc'] == 'x'


@pytest.mark.azul
def test_post_clean_floor():
    """Очистка линии пола"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floortwo:x'),
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

    assert post_response['floorone'].export() == 'floorone:'
    assert post_response['floortwo'].export() == 'floortwo:'
    assert post_response['command']['floor_clear'] == '+'


@pytest.mark.azul
def test_post_reducing_contents_of_bag():
    """Уменьшение содержимого мешка"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floortwo:x'),
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

    export_bag = re.compile(r"^(bag:\w{80})")

    assert len(post_response['bag']) == 80
    assert export_bag.match(post_response['bag'].export()) is not None


@pytest.mark.azul
def test_post_enlarge_contents_of_box():
    """Увеличение содержимое коробки"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floortwo:x'),
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

    export_box = re.compile(r"^(box:\w{9})")

    assert len(post_response['box']) == 9
    assert post_response['box'].elements.count('r') == 2
    assert post_response['box'].elements.count('d') == 5
    assert post_response['box'].elements.count('y') == 2
    assert post_response['box'].elements.count('x') == 0
    assert export_box.match(post_response['box'].export()) is not None



@pytest.mark.azul
def test_post_change_first_player():
    """Ходит тот игрок у кого был жетон первого игрока (Не важно кто последний сделал ход)"""
    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:'),
        floortwo=models.Floor.imports(elements='floortwo:x'),
        wallone=models.Wall.new('one'),
        walltwo=models.Wall.new('two'),
        table=models.Table.imports(tiles='table:y'),
        box=models.Box.new(),
        bag=models.Bag.new(),
        kind='kind:one.Hokage,two.Omoluzu',
        active=models.Active.imports(element='active:one'),
        first_player=models.FirstPlayer.imports(element='first_player:one')
    )

    info = {
        'command': 'post',
        'fact': 0,
        'color': 'y',
        'line': 5,
        'player': 'one'
    }

    post_response = azul.post(info=info)
    assert post_response['first_player'].export() == 'first_player:two'
    assert post_response['command']['change_first_player'] == 'two'

    azul = view.Azul(
        factory=models.Factories.imports(fact='fact:-.-.-.-.-'),
        patternone=models.Pattern.imports(pattern='patternone:g.rr.ddd.dddd.-----'),
        patterntwo=models.Pattern.imports(pattern='patterntwo:d.rr.yyy.---g.---bb'),
        floorone=models.Floor.imports(elements='floorone:x'),
        floortwo=models.Floor.imports(elements='floortwo:'),
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
    assert post_response['first_player'].export() == 'first_player:one'
    assert post_response['command']['change_first_player'] == 'one'



# todo Подсчет и сохранение кол-ва победных очков
# todo Если на линии пола были лишние плитки, они должны положиться в box
