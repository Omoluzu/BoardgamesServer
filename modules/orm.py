# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

DeclarativeBase = declarative_base()


class Users(DeclarativeBase):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(90))  # Логин пользователя
    password = Column(Binary)  # Пароль пользователя
    active = Column(Boolean)  # Проверка на то активирован ли пользователь


class ORM:
    """ Класс для работы с ORM """
    databases = None

    def __init__(self):

        _engine = create_engine(URL(**settings.DATABASE))
        DeclarativeBase.metadata.create_all(_engine)
        _Session = sessionmaker(bind=_engine)
        ORM.databases = _Session()
