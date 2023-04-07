from enum import IntEnum, auto


class Tile(IntEnum):
    NONE = 0
    FIRST_PLAYER = auto()
    BLACK = auto()
    BLUE = auto()
    DARK_BLUE = auto()
    YELLOW = auto()
    RED = auto()
