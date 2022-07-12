# -*- coding: utf-8 -*-
from pprint import pprint

from modules.ORM.ListGames import ListGames


def game_over(data: dict) -> dict:
    """
    Завершение игры
    """

    ListGames.del_games(game_id=data['game_id'])

    return {}
