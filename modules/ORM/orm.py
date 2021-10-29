# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

DeclarativeBase = declarative_base()


class UsersDB(DeclarativeBase):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(90))  # Логин пользователя
    password = Column(LargeBinary)  # Пароль пользователя
    active = Column(Boolean)  # Проверка на то активирован ли пользователь


class ListGamesDB(DeclarativeBase):

    __tablename__ = "list_games"

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_user_id = Column(Integer, ForeignKey(UsersDB.id))
    games = Column(String(60))
    games_config = Column(Text)


class ORM:
    """ Класс для работы с ORM """
    config = None
    databases = None

    if not databases:
        _engine = create_engine(URL(**settings.DATABASE))
        DeclarativeBase.metadata.create_all(_engine)
        _Session = sessionmaker(bind=_engine)
        databases = _Session()
