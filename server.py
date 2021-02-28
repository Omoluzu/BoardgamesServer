#
# Серверное приложение для соединений
#

import json
import asyncio
from typing import Optional


class ServerProtocol(asyncio.Protocol):
    server: 'Server'
    transport: asyncio.transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        data_deocde = json.loads(data.decode())
        if data_deocde['type'] == "auth":
            print("Запрос на авторизацию")
            new_data = self._check_auth(data_deocde)
            self.send_message(new_data)
        else:
            self.send_message(data)

    def connection_made(self, transport: asyncio.transports.Transport):
        self.server.clients.append(self)
        self.transport = transport

        print("Пришел новый клиент")

    def connection_lost(self, exc: Optional[Exception]):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: bytes):
        """ Возврат сообщения всем пользователям """
        for user in self.server.clients:
            user.transport.write(content)

    @staticmethod
    def _check_auth(data: dict):
        """ Проверка на авторизацию """
        data['auth'] = True
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