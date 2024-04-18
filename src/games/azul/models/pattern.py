from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    line1: str
    line2: str
    line3: str
    line4: str
    line5: str
    excess_tile: int = 0
    put_tile: int = 0

    @classmethod
    def imports(cls, pattern: str) -> 'Pattern':
        """Импортирование текущего состояния планшета игрока размещений линий

        Args:
            pattern:
                Текущее состояния планшета
                patternone:-.--.-rr.----.-----
        """
        name, info = (pattern.split(':'))
        return cls(name, *info.split('.'))

    def __repr__(self):
        return (f"Pattern(name='{self.name}', line1='{self.line1}', "
                f"line2='{self.line2}', line3='{self.line3}', "
                f"line4='{self.line4}', line5='{self.line5}')")

    def post_tile(self, line: int, tiles: str) -> None:
        """Выставление плиток на планшет игрока

        Args:
            line:
                Линия для размещения.
                3
            tiles:
                Плитки для размещения
                'rrr'
        """

        pattern: str = getattr(self, f"line{line}")[::-1]
        excess_tile = len(tiles) - pattern.count('-')
        self.excess_tile = excess_tile if excess_tile > 0 else 0
        self.put_tile = len(tiles) - self.excess_tile
        lines = pattern.replace('-', tiles[0], self.put_tile)
        setattr(self, f"line{line}", lines[::-1])

    def export(self) -> str:
        """Экспорт содержимого

        Returns:
            'patternone:-.--.-rr.----.-----'
            'patterntwo:-.--.-rr.----.-----'
        """
        return f"{self.name}:{self.line1}.{self.line2}.{self.line3}.{self.line4}.{self.line5}"


if __name__ == '__main__':
    patterns = Pattern.imports(pattern='patternone:-.--.-rr.---r.-----')
    patterns.post_tile(line=2, tiles='rrrrrrrrrr')
    # patterns.post_tile(line=3, tiles='r')
    # patterns.post_tile(line=4, tiles='rr')
    # patterns.post_tile(line=5, tiles='rrr')
    print(patterns.export())
    print(patterns.excess_tile)
    print(patterns.put_tile)
    # print(patterns)
