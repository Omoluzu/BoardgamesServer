from src.games.azul.view import Azul
from src.games.azul.models import Factories, Pattern


def test_standard_post_tile():
    azul = Azul(
        factory=Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr'),
        patternone=Pattern.imports(pattern='patternone:-.--.---.----.-----'),
        patterntwo=Pattern.imports(pattern='patterntwo:-.--.---.----.-----')
    )

    info = {
        'command': 'post',
        'fact': '5',
        'color': 'r',
        'line': '3',
        'player': 'one'
        # 'user': 'Omoluzu'
    }

    post_response = azul.post(info=info)
    assert post_response['fact'].factory[4].export() == '-'
    assert post_response['fact'].export() == 'fact:rgyd.rygd.dggb.bygb.-'
    assert post_response['command']['clean_fact'] == 5
    assert post_response['command']['add_desc'] == 'yd'
    assert post_response['command']['count'] == 2
    assert post_response['command']['post_pattern_line'] == 'line.3,player.one,tile.r,count.2'
    assert post_response['patternone'].export() == 'patternone:-.--.-rr.----.-----'

    info = {
        'command': 'post',
        'fact': '4',
        'color': 'y',
        'line': '1',
        'player': 'two'
        # 'user': 'Omoluzu'
    }

    post_response = azul.post(info=info)
    assert post_response['fact'].factory[3].export() == '-'
    assert post_response['fact'].export() == 'fact:rgyd.rygd.dggb.-.-'
    assert post_response['command']['clean_fact'] == 4
    assert post_response['command']['add_desc'] == 'bgb'
    assert post_response['command']['count'] == 1
    assert post_response['command']['post_pattern_line'] == 'line.1,player.two,tile.y,count.1'
    assert post_response['patterntwo'].export() == 'patterntwo:y.--.---.----.-----'



test_standard_post_tile()
