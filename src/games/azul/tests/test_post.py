from src.games.azul.view import Azul
from src.games.azul.models import Factories


def test_standard_post_tile():
    azul = Azul(
        factory=Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr')
    )

    info = {
        'command': 'post',
        'fact': '5',
        'color': 'r',
        'line': '3',
        # 'user': 'Omoluzu'
    }

    post_response = azul.post(info=info)
    assert post_response['fact'].factory[4].export() == '-'
    assert post_response['fact'].export() == 'fact:rgyd.rygd.dggb.bygb.-'
    assert post_response['command']['clean_fact'] == 5
    assert post_response['command']['add_desc'] == 'yd'
    assert post_response['command']['count'] == 2

    info = {
        'command': 'post',
        'fact': '4',
        'color': 'y',
        'line': '1',
        # 'user': 'Omoluzu'
    }

    post_response = azul.post(info=info)
    assert post_response['fact'].factory[3].export() == '-'
    assert post_response['fact'].export() == 'fact:rgyd.rygd.dggb.-.-'
    assert post_response['command']['clean_fact'] == 4
    assert post_response['command']['add_desc'] == 'bgb'
    assert post_response['command']['count'] == 1


test_standard_post_tile()
