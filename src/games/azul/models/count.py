from dataclasses import dataclass

from src import models


@dataclass
class Count(models.BaseString):
    name: str = 'count'

    @classmethod
    def new(cls, suffix: str) -> 'Count':  # noqa
        return cls(name=f"count{suffix}", element='0|0')

    @classmethod
    def imports(cls, element: str) -> 'Count':
        name, _element = element.split(':')
        return cls(name=name, element=_element)

    def update(self, value: int) -> None:
        element, _ = self.element.split('|')

        self.element = f"{(int(element) + value)}|{value}"
