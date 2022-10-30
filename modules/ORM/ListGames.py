# -*- coding: utf-8 -*-

"""
Модуль для работы с БД LisGames
"""

import os
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

        user = Users.get_user(name_user=data['user'])
        new_games.users.append(user)

        cls.databases.add(new_games)
        cls.databases.commit()

        data['games_id'] = new_games.id

        return data

    @classmethod
    def join_game(cls, data):
        """ ДОбавление пользователя к игре """

        user = Users.get_user(name_user=data['user'])
        game = cls.databases.query(ListGamesDB).filter_by(id=data['game_id']).one()
        game.users.append(user)

        if json.loads(game.games_config)['select_players'] == len(game.users):
            game.status = "Active"

        cls.databases.commit()

    @classmethod
    def get_path_games(cls, id_games) -> str:
        """
        Запрос пути сохранения игры

        :param id_games:
        :return:
        """
        games = cls.databases.query(ListGamesDB).filter_by(id=id_games).one()
        return os.path.join("GameSave", (os.path.join(games.games, f"{games.id}.csv")))
        # return os.path.join("GameSave", games.games)

    @classmethod
    def get_games_info(cls, games_id) -> dict:
        """
        Запрос на получение информации конкретной игры
        :param games_id:
        :return:
        """
        games = cls.databases.query(ListGamesDB).filter_by(id=games_id).one()

        return {
            "create_user": Users.get_user_name(games.create_user_id),
            "games_config": json.loads(games.games_config),
            "games": games.games,
            "users": list(Users.get_user_name(user.id) for user in games.users)
        }

    @classmethod
    def get_current_action_games(cls) -> dict:
        """
        Возврат списка активных игр
        :return:
        """
        list_games = []

        for games in cls.databases.query(ListGamesDB).all():
            if not games.canceled:
                list_games.append({
                    "id": games.id,
                    "status": games.status,
                    "create_user": Users.get_user_name(games.create_user_id),
                    "games": games.games,
                    "games_config": games.games_config,
                    "users": list(Users.get_user_name(user.id) for user in games.users)
                })

        return {
            "command": "update_list_games",
            "list_games": list_games,
        }

    @classmethod
    def del_games(cls, game_id) -> None:
        """
        Пометка о завершении игры в БД
        :param game_id:
        :return:
        """

        game = cls.databases.query(ListGamesDB).filter_by(id=game_id).one()
        game.canceled = True
        cls.databases.commit()
