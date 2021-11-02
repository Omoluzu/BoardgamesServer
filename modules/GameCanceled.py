# -*- coding: utf-8 -*-

"""
Запрос на удаление текущей игрыы
"""

from modules.ORM.ListGames import ListGames


def game_canceled(info) -> tuple:

    message = {
        "command": "message",
        "message": f"Пользователь <b>{info['user']}</b> отменил игру: {info['games']}",
        "user": "System"
    }

    ListGames.del_games(info['game_id'])

    return message, ListGames.get_current_action_games()



