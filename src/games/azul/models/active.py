from dataclasses import dataclass

from src import models


SELECT = ('one', 'two', )


@dataclass
class Active(models.BaseString):
    name: str = 'active'

    @classmethod
    def new(cls) -> 'Active':
        return cls(element='one')

    def change_player(self) -> None:
        index = SELECT.index(self.element)
        try:
            self.element = SELECT[index + 1]
        except IndexError:
            self.element = SELECT[0]
