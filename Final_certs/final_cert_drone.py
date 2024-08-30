import asyncio
import websockets
import jwt
import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# Конфигурация
SERVER_URL = "ws://localhost:8765"
SECRET_KEY = 'my_secret_key'  # Должен совпадать с сервером
USERNAME = 'drone1'
PASSWORD = '333'

# Функция для создания JWT токена
def create_jwt_token(username, secret_key):
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
    }, secret_key, algorithm="HS256")
    return token

async def websocket_client():
    async with websockets.connect(SERVER_URL) as websocket:
        # Отправка данных для авторизации
        auth_message = f'LOGIN:{USERNAME},{PASSWORD}'
        await websocket.send(auth_message)
        logging.info(f"Sent to server: {auth_message}")

        # Ожидание ответа от сервера на авторизацию
        auth_response = await websocket.recv()
        logging.info(f"Received from server: {auth_response}")

        if auth_response.startswith("JWT:"):
            logging.info("Authorization successful. Waiting for commands...")

            while True:
                try:
                    # Ожидание команды от сервера
                    command_message = await websocket.recv()
                    logging.info(f"Received command: {command_message}")

                    if command_message.startswith("COMMAND:"):
                        command = command_message.split(":")[1]

                        if command == "takeoff":
                            response = "Drone is taking off"
                        elif command == "land":
                            response = "Drone is landing"
                        else:
                            response = f"Unknown command: {command}"
                        logging.info(response)

                        # Отправка ответа серверу
                        await websocket.send(f"Response: {response}")

                except websockets.ConnectionClosedError:
                    logging.error("Connection with server lost.")
                    break

        else:
            logging.error("Authorization failed.")

# Запуск клиента
asyncio.get_event_loop().run_until_complete(websocket_client())
