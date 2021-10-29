#
# Серверное приложение для соединений
#

import json
import asyncio
from typing import Optional

from modules.ORM.orm import *
import modules


class ServerProtocol(asyncio.Protocol, ORM):
    server: 'Server'
    transport: asyncio.transports.Transport

    def __init__(self, server: 'Server'):
        super().__init__()
        self.server = server

    def data_received(self, data: bytes):
        data_decode = json.loads(data.decode())
        if data_decode['type'] == "auth":
            new_data = self._check_auth(data_decode)
            self.send_message(new_data, command='self')
        elif data_decode['type'] == "register":
            new_data = self._check_register(data_decode)
            self.send_message(new_data, command='self')
        elif data_decode['type'] == "message":
            self.send_message(data_decode)
        elif data_decode['type'] == "create_games":
            self.send_message(modules.create_games(data_decode))
            self.send_message({
                "type": "message",
                "message": f"Пользователь {data_decode['user']}: Создал игру {data_decode['ru']}",
                "user": "System"
            })
        else:
            new_data = data_decode
            print(f"Ко мне пришло непонятное сообщение: {data_decode['type']} = {data_decode}")
            self.send_message(new_data)

    def connection_made(self, transport: asyncio.transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")

    def connection_lost(self, exc: Optional[Exception]):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: dict, command: str = None):
        """ Возврат сообщения всем пользователям """
        data = json.dumps(content).encode()

        for user in self.server.clients:
            if command == "self":  # Отправка сообщения только клиенту который общался с сервером
                if self == user:
                    user.transport.write(data)
                    break
            else:  # Отправка сообщения всем пользователям
                user.transport.write(data)

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
