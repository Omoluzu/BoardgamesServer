"""Игровая коробка для хранения сброшенных плиток"""
from dataclasses import dataclass

from src import models


@dataclass
class Box(models.BaseList):
    name: str = 'box'
