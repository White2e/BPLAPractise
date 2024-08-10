# pip install websockets asyncio
#
import websockets, asyncio, logging
from urllib.parse import urlparse, parse_qs


# логгирование
logging.basicConfig(level=logging.INFO, filemode="w")


class SecureProxy:
    def __init__(self, control_drone):
        self._control_drone = control_drone

    async def __call__(self, websocket, path):
        async for msg in websocket:
            if self.is_auth(websocket):
                await self._control_drone(websocket, path, msg)
            else:
                logging.info("Client not authorized")
                await websocket.send("Unauthorized access")
                await websocket.close(code=403, reason="Forbidden")
                return

    def is_auth(self, websocket):
        # проверка авторизации
        # здесь должна быть реализация проверки авторизации
        # например, чтение из файла или проверка существования токена
        # return True if авторизация прошла успешно, False в противном случае
        #print(websocket.path)
        url = websocket.path
        # Разбор URL
        parsed_url = urlparse(url)
        # Извлечение параметров запроса
        query_params = parse_qs(parsed_url.query)
        # Получение значения токена
        token = query_params.get('token', [None])[0]
        print(f"Token: {token}")
        params = dict(token=token)
        return params.get("token") == "valid_token"



async def control_drone(websocket, path, msg):
    try:
        logging.info(f"Received from client: {msg}")
        print(f"Received from client: {msg}")
        if msg == 'takeoff':
            logging.info('Drone is taking off')
            await websocket.send('Drone is taking off')
        if msg == 'land':
            logging.info('Drone is landing')
            await websocket.send('Drone is landing')
    except websockets.ConnectionClosedError as e:
        logging.info(f"Client disconnected. {e}")
    except Exception as e:
        logging.info(f"An error occurred: {e}")


async def main():
    # передаем ссылку на функцию
    proxy = SecureProxy(control_drone)
    logging.info("Starting WebSocket server...")
    async with websockets.serve(proxy, "localhost", 8765) as server:
        try:
            logging.info("WebSocket server started")
            await server.wait_closed()
            # await server.serve_forever()
            # await asyncio.Future()
        except Exception as e:
            logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
