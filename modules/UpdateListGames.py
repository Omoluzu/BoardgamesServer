# -*- coding: utf-8 -*-

"""
Запрос на обновление списка активныз игр
"""

from modules.ORM.ListGames import ListGames


def update_list_games() -> dict:
    """ Запрос на обновление списка активныз игр """
    return ListGames.get_current_action_games()
