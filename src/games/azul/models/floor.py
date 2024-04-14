"""Описание логики игры с игровым столом"""
from dataclasses import dataclass

from src import models


@dataclass
class Floor(models.BaseList):
    name: str = 'floor'

    @classmethod
    def imports(cls, elements: str) -> 'Floor':
        """Импортирование текущего состояния линии пола

        Args:
            elements:
                Текущее состояния линии пола
                'floorone:x'
        """
        name, elements = elements.split(':')
        return cls(name=name, elements=list(elements))
