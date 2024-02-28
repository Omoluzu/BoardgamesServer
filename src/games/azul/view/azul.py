import re

from dataclasses import dataclass

from src.games.azul.models import Factories


REGULAR = r'(?P<fact>fact:[^;]*)'


@dataclass
class Azul:
    factory: Factories

    @classmethod
    def open_save(cls, game_id, test=False) -> 'Azul':
        from modules.GameInformation import game_information

        game = game_information(data={'game_id': game_id}, test=test)
        match_game_info = re.match(REGULAR, game['game_info'])

        return cls(
            factory=Factories.imports(match_game_info.group('fact'))
        )

    def post(self, info):
        data = self.factory.get_tile(
            factory_number=int(info['fact']),
            tile=info['color']
        )

        return {
            'fact': self.factory,
            'command': {
                'clean_fact': int(info['fact']),
                **data
            }
        }
