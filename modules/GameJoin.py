# -*- coding: utf-8 -*-

"""
Запрос на присоединение пользователя к игре
"""

from modules.ORM.ListGames import ListGames


def game_join(data: dict) -> tuple:

    message_chat = {
        "command": "message",
        "message": f"Пользователь <b>{data['user']}</b>: присоединился к игре {data['games']}",
        "user": "System"
    }

    ListGames.join_game(data)

    return message_chat, ListGames.get_current_action_games()
