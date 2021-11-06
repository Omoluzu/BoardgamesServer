# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

import settings


DeclarativeBase = declarative_base()

association_table = Table(
    'association', DeclarativeBase.metadata,
    Column('list_game_id', ForeignKey('list_game.id'), primary_key=True),
    Column('user_id', ForeignKey('user.id'), primary_key=True),
)


class UsersDB(DeclarativeBase):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(90))  # Логин пользователя
    password = Column(LargeBinary)  # Пароль пользователя
    active = Column(Boolean)  # Проверка на то активирован ли пользователь

    list_games = relationship(
        "ListGamesDB",
        secondary=association_table,
        back_populates="users",
        passive_deletes=True
    )


class ListGamesDB(DeclarativeBase):

    __tablename__ = "list_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(30), default="Await")  # Статус игры. Такие как Ожидание игроков, Активно (Играется).
    create_user_id = Column(Integer, ForeignKey(UsersDB.id))
    games = Column(String(60))
    games_config = Column(Text)
    canceled = Column(Boolean, default=False)  # Временная колонка для пометки игры на удаление
    users = relationship(
        "UsersDB",
        secondary=association_table,
        back_populates="list_games",
        cascade="all, delete",
    )

    """
    status
        Await: - В ожидании игроков
        Active: - Игра играется игроками
    """


class ORM:
    """ Класс для работы с ORM """
    config = None
    databases = None

    if not databases:
        _engine = create_engine(URL(**settings.DATABASE))
        DeclarativeBase.metadata.create_all(_engine)
        _Session = sessionmaker(bind=_engine)
        databases = _Session()
