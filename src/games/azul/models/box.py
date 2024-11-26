"""Игровая коробка для хранения сброшенных плиток"""
from dataclasses import dataclass

from src import models


@dataclass
class Box(models.BaseList):
    name: str = 'box'

    def add_element_before_post_wall(
            self, element_player_one: list[str], element_player_two: list[str]
    ) -> None:
        """Складирование плиток в коробку после выкладывание их на стену
        игроками

        Args:
            element_player_one: Содержимое выставленных плиток первым игроком
                ['g', 'r', 'd', 'd', '-']
            element_player_two: Содержимое выставленных плиток вторым игроком
                ['d', 'r', 'y', '-', '-']
        """
        for player in [element_player_one, element_player_two]:
            for i, element in enumerate(player):
                if element != '-':
                    self.element_add(element=element * i)