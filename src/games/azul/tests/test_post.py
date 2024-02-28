from src.games.azul.view import Azul
from src.games.azul.models import Factories


def test_first():
    azul = Azul(
        factory=Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr')
    )

    info = {
        'command': 'post',
        'fact': '5',
        'color': 'r',
        'line': '3',
        # 'game_id': 1,
        # 'user': 'Omoluzu'
    }

    post_response = azul.post(info=info)
    assert post_response['fact'].factory[4].export() == '-'
    assert post_response['command']['clean_fact'] == 5
    assert post_response['command']['desc'] == 'yd'
    assert post_response['command']['count'] == 2


def test_second():
    azul = Azul(
        factory=Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr')
    )

    info = {
        'command': 'post',
        'fact': '4',
        'color': 'y',
        'line': '1',
        # 'game_id': 1,
        # 'user': 'Omoluzu'
    }

    post_response = azul.post(info=info)
    assert post_response['fact'].factory[3].export() == '-'
    assert post_response['command']['clean_fact'] == 4
    assert post_response['command']['desc'] == 'bgb'
    assert post_response['command']['count'] == 1


test_first()
test_second()
