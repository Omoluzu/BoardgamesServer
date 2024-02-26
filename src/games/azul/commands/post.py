

def post(info):
    print(info)


if __name__ == '__main__':
    from src.games.azul.models import Factories

    fact = Factories.imports(fact='fact:rgyd.rygd.dggb.bygb.yrdr')

    print(fact.export())


    # info = {
    #     'command': 'post',
    #     'fact': '5',
    #     'color': 'r',
    #     'line': '3',
    #     'game_id': 1,
    #     'user': 'Omoluzu'
    # }
    #
    # print(info)