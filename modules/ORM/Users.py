# -*- coding: utf-8 -*-

"""
Модуль для работы с БД Users
"""

from modules.ORM.orm import ORM
from modules.ORM.orm import UsersDB


class Users(ORM):

    @classmethod
    def get_user_id(cls, user_name: str) -> int:
        """ Получение ИД пользователя """
        return cls.databases.query(UsersDB).filter_by(login=user_name).one().id

    @classmethod
    def get_user_name(cls, user_id: int) -> str:
        """ Получение имени пользователя """
        return cls.databases.query(UsersDB).filter_by(id=user_id).one().login
