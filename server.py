#
# Серверное приложение для соединений
#

import json
import asyncio
from typing import Optional

from modules.ORM.orm import *
import modules

from modules.ORM.ListGames import ListGames


COMMAND = {
    "create_games": modules.create_games,
    "user_connect": modules.user_connect,
    "game_canceled": modules.game_canceled,
    "message": modules.message,
    "game_join": modules.game_join,
    "information_games": modules.game_information,
}


class ServerProtocol(asyncio.Protocol, ORM):
    server: 'Server'
    transport: asyncio.transports.Transport

    def __init__(self, server: 'Server'):
        super().__init__()
        self.server = server

    def data_received(self, data: bytes):
        data_decode = json.loads(data.decode())
        print(f">> Получен запрос от клиента: {data_decode}")

        match data_decode['command']:
            case "auth":
                self.send_message(self._check_auth(data_decode), command='self')
            case "register":
                self.send_message(self._check_register(data_decode), command='self')
            case "update_list_games":
                self.send_message(modules.update_list_games(), command='self')
            case _:
                if command := COMMAND.get(data_decode['command']):
                    self.send_message(command(data_decode))
                else:
                    print(f"Ко мне пришло непонятное сообщение: {data_decode['command']} = {data_decode}")

    def connection_made(self, transport: asyncio.transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")

    def connection_lost(self, exc: Optional[Exception]):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, *args, command: str = None, ):
        """ Отправка сообщений клиенту

        :param command: Управление отправкой сообщений. Может принимать следующий команды
            :self: Отправка сообщения только пользователю который выполнил запрос к БД
        """
        def send_message_user(users, content):
            for data in content:
                if type(data) is tuple:
                    send_message_user(users, *content)
                else:
                    print(f"<< Отправка сообщения клиенту: {data}")
                    users.transport.write(json.dumps(data).encode())

        for user in self.server.clients:
            if command == "self":  # Отправка сообщения только клиенту который общался с сервером
                if self == user:
                    send_message_user(user, args)
                    break
            else:  # Отправка сообщения всем пользователям
                send_message_user(user, args)

    def _check_auth(self, data: dict):
        """ Проверка на авторизацию """
        user_db = self.databases.query(UsersDB).filter_by(login=str(data['login'])).all()
        if user_db:
            if data['password'] == user_db[0].password.decode():
                data['auth'] = True
            else:
                data['auth'] = False
                data['exception'] = "Введен неправильный пароль"
        else:
            data['auth'] = False
            data['exception'] = "Нету такого пользователя в базе данных"

        return data

    def _check_register(self, data: dict):
        """ Регистрация нового пользователя """
        user_db = self.databases.query(UsersDB).filter_by(login=str(data['login'])).all()
        if not user_db:
            self.databases.add(UsersDB(
                login=data['login'],
                password=data['password'].encode(),
                active=True
            ))
            self.databases.commit()
            data['register'] = True
        else:
            data['register'] = False
            data['exception'] = "Имя уже занято"

        return data


class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            "127.0.0.1",
            8888
        )

        print("Сервер запущен ... ")

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер отстановлен вручную")
