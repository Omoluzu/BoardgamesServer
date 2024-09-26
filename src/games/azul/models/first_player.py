from dataclasses import dataclass

from src import models


@dataclass
class FirstPlayer(models.BaseString):
	name: str = 'first_player'

	@classmethod
	def new(cls) -> 'FirstPlayer':
		return cls(element='one')

	def change_first_player(self, value: str) -> None:
		"""Change first player
		:param value: New first player
		"""
		self.element = value
