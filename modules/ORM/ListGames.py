# -*- coding: utf-8 -*-

"""
Модуль для работы с БД LisGames
"""

import json
from pprint import pprint

from modules.ORM.orm import ORM, ListGamesDB
from modules.ORM.Users import Users


class ListGames(ORM):

    @classmethod
    def create_new_games(cls, data: dict) -> dict:
        """
        Сохранение информации о новой игре в базу данных,
        и возврат ИД созданной игры

        :param data: Информация об игре полученная от клиента
        :return:
        """

        new_games = ListGamesDB(
            create_user_id=Users.get_user_id(data['user']),
            games=data['games'],
            games_config=json.dumps(data['games_config']),
        )

        cls.databases.add(new_games)
        cls.databases.commit()

        data['games_id'] = new_games.id

        return data

    @classmethod
    def get_current_action_games(cls) -> dict:
        """
        Возврат списка активных игр
        :return:
        """
        list_games = []

        for games in cls.databases.query(ListGamesDB).all():
            list_games.append({
                "id": games.id,
                "user": Users.get_user_name(games.create_user_id),
                "games": games.games,
                "games_config": games.games_config,
            })

        return {
            "command": "update_list_games",
            "list_games": list_games,
        }

    @classmethod
    def del_games(cls, game_id) -> None:
        """
        Удаление информации об игре из БД
        :param game_id:
        :return:
        """
        cls.databases.query(ListGamesDB).filter_by(id=game_id).delete()