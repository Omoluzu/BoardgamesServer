"""Описание логики игры с игровым столом"""
from dataclasses import dataclass

from src.games.azul import models


@dataclass
class Floor(models.BaseList):
    name: str = 'floor'
