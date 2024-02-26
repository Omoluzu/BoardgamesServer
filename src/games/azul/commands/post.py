from src.games.azul.models import Factories


def post(fact: Factories, info):
    data = fact.get_tile(factory_number=int(info['fact']), tile=info['color'])

    return {
        'fact': fact,
        'command': {
            'fact': int(info['fact']),
            **data
        }
    }


if __name__ == '__main__':
    fact1 = Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr')
    info1 = {
        'command': 'post',
        'fact': '5',
        'color': 'r',
        'line': '3',
        # 'game_id': 1,
        # 'user': 'Omoluzu'
    }

    p1 = post(fact=fact1, info=info1)
    assert p1['fact'].factory[4].export() == '-'
    assert p1['command']['fact'] == 5
    assert p1['command']['desc'] == 'yd'
    assert p1['command']['count'] == 2

    fact2 = Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr')
    info2 = {
        'command': 'post',
        'fact': '4',
        'color': 'y',
        'line': '1',
        # 'game_id': 1,
        # 'user': 'Omoluzu'
    }

    p2 = post(fact=fact2, info=info2)
    assert p2['fact'].factory[3].export() == '-'
    assert p2['command']['fact'] == 4
    assert p2['command']['desc'] == 'bgb'
    assert p2['command']['count'] == 1

    print(p1)
    print(p2)