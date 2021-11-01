# -*- coding: utf-8 -*-

"""
Запрос на удаление текущей игрыы
"""

from modules.ORM.ListGames import ListGames


def game_canceled(info) -> dict:

    message = {
        "command": "message",
        "message": f"Пользователь <b>{info['user']}</b> отменил игру: {info['games']}",
        "user": "System"
    }

    return message



