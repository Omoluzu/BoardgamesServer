# -*- coding: utf-8 -*-

"""
Модуль для работы с БД LisGames
"""

import json
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
