import re

from dataclasses import dataclass

from src.games.azul.models import Factories, Pattern


# REGULAR = r'(?P<fact>fact:[^;]*)'
REGULAR = r'(?P<fact>fact:[^;]*);(?P<patternone>patternone:[^;]*);(?P<patterntwo>patterntwo:[^;]*);(?P<kind>kind:[^;]*)'


@dataclass
class Azul:
    factory: Factories
    patternone: Pattern
    patterntwo: Pattern

    @classmethod
    def open_save(cls, game_id, test=False) -> 'Azul':
        from modules.GameInformation import game_information

        game = game_information(data={'game_id': game_id}, test=test)
        match_game_info = re.match(REGULAR, game['game_info'])

        return cls(
            factory=Factories.imports(match_game_info.group('fact')),
            patternone=Pattern.imports(match_game_info.group('patternone')),
            patterntwo=Pattern.imports(match_game_info.group('patterntwo'))
        )

    def post(self, info: dict) -> dict:
        data = self.factory.get_tile(
            factory_number=int(info['fact']),
            tile=info['color']
        )
        pattern = getattr(self, f"pattern{info['player']}")
        pattern.post_tile(
            line=info['line'],
            tiles=info['color'] * data['count']
        )

        return {
            'fact': self.factory,
            'patternone': self.patternone,
            'patterntwo': self.patterntwo,
            'command': {
                'clean_fact': int(info['fact']),
                'post_pattern_line': f"line.{info['line']},player.{info['player']},tile.{info['color']},count.{data['count']}",
                **data
            }
        }
