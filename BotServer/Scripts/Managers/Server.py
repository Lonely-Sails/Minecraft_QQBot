from ..Config import config
from ..Utils import decode, encode
from .Data import data_manager

from nonebot.log import logger
from nonebot.drivers import WebSocket
from nonebot.exception import WebSocketClosed

from typing import Union
from json import dumps, loads


class Server:
    name: str = None
    type: str = None
    status: bool = True
    websocket: WebSocket = None

    def __init__(self, name: str, websocket: WebSocket):
        self.name = name
        self.websocket = websocket
        self.type = websocket.request.headers.get('type')

    async def disconnect(self):
        self.status = False
        await self.websocket.close()
        logger.success(F'已断开与服务器 [{self.name}] 的连接！')

    async def send_data(self, event_type: str, data: dict = {}):
        try:
            await self.websocket.send(decode(dumps({'type': event_type, 'data': data})))
            logger.debug(F'已向服务器 [{self.name}] 发送数据 {data}，正在等待回应……')
            response = loads(encode(await self.websocket.receive()))
            if response.get('success'):
                logger.debug(F'已收到服务器 [{self.name}] 的回应 {response}，数据发送成功！')
                return response.get('data')
        except (WebSocketClosed, ConnectionError):
            self.status = False
            logger.warning(F'与服务器 [{self.name}] 的连接已断开！')
            return None

    async def send_command(self, command: str):
        if response := await self.send_data('command', {'command': command}):
            return response.get('response', {})

    async def send_message(self, message: str):
        return await self.send_data('message', {'message': message})

    async def send_player_list(self):
        return await self.send_data('player_list')


class ServerManager:
    servers: dict[str, Server] = {}

    def check_online(self):
        return any(server.status for server in self.servers.values())

    def append_server(self, name: str, websocket: WebSocket):
        self.servers[name] = Server(name, websocket)

    def get_server(self, server_flag: Union[str, int]):
        if isinstance(server_flag, int) or server_flag.isdigit():
            index = int(server_flag)
            if index > len(data_manager.servers):
                return None
            server_flag = data_manager.servers[index - 1]
        server = self.servers.get(server_flag)
        if isinstance(server, Server) and server.status:
            return server

    async def disconnect_server(self, name: str):
        if server := self.servers.get(name):
            await server.disconnect()

    async def unload(self):
        logger.info('正在断开所有服务器的连接……')
        for server in self.servers.values():
            await server.disconnect()
        logger.success('所有服务器的连接已断开！')

    async def execute(self, command: str, server_flag: Union[str, int] = None):
        if not server_flag:
            logger.debug(F'执行命令 [{command}] 到所有已连接的服务器。')
            return {name: await server.send_command(command) for name, server in self.servers.items() if server.status}
        if server := self.get_server(server_flag):
            logger.debug(F'执行命令 [{command}] 到服务器 [{server.name}]。')
            return await server.send_command(command)

    async def broadcast(self, source: str, player: str = None, message: str = None, except_server: str = None):
        params = [{'color': config.sync_color_source, 'text': F'[{source}] '}]
        if player: params.append({'color': config.sync_color_player, 'text': F'<{player}> '})
        if message: params.append({'color': config.sync_color_message, 'text': message})
        command = F'tellraw @a {dumps(params)}'
        if not except_server:
            await self.execute(command)
            return None
        for name, server in self.servers.items():
            if name != except_server and server.status:
                await server.send_command(command)


server_manager = ServerManager()
