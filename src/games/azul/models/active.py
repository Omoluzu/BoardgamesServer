from dataclasses import dataclass


SELECT = ('one', 'two', )


@dataclass
class Active:
    player: str

    @classmethod
    def new(cls) -> 'Active':
        return cls(player='one')

    @classmethod
    def imports(cls, active: str) -> 'Active':
        active = active.replace('active:', '')
        return cls(player=active)

    def change_player(self) -> None:
        index = SELECT.index(self.player)
        try:
            self.player = SELECT[index + 1]
        except IndexError:
            self.player = SELECT[0]

    def export(self) -> str:
        return f"active:{self.player}"

