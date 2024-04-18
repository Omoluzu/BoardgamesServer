"""Описание логики игры с игровым столом"""
from dataclasses import dataclass

from src import models


@dataclass
class Floor(models.BaseList):
    name: str = 'floor'
    suffix = True
    limit = 7
