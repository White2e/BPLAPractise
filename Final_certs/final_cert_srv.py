import asyncio
import time
import websockets
import jwt
import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# Секретный ключ для подписи JWT-токенов
SECRET_KEY = 'my_secret_key'

# Простая база данных пользователей
users_db = {
    "user1": "111",
    "user2": "222",
    "drone1": "333",
    "drone2": "444",
}

connected_drones = {}  # Для отслеживания подключенных дронов
connected_users = {}  # Для отслеживания подключенных операторов

# Функция для создания JWT-токена
def create_jwt_token(username):
    payload = {
        "sub": username,
        "iat": datetime.datetime.now(datetime.timezone.utc),
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Функция для проверки JWT-токена
def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Обработка WebSocket-соединений
async def handle_client(websocket, path):
    async for data in websocket:
        if data.startswith("LOGIN:"):
            credentials = data[6:].split(",")
            username = credentials[0]
            password = credentials[1]
            logging.info(f'Login attempt: {username}')

            if username in users_db and users_db[username] == password:
                token = create_jwt_token(username)
                await websocket.send(f"JWT:{token}")
                logging.info(f'Token sent: {token}')

                # Сохраняем WebSocket соединение дрона
                if username.startswith('drone'):
                    connected_drones[username] = websocket
                    logging.info(f'Drone: {username} connected')
                # Сохраняем WebSocket соединение оператора
                if username.startswith('user'):
                    connected_users[username] = websocket
                    logging.info(f'Operator: {username} connected')

            else:
                await websocket.send("ERROR: Неверные имя пользователя или пароль")

        elif data.startswith("COMMAND:"):
            credentials = data[8:].split(",")
            token = credentials[0]
            command = credentials[1]

            username = verify_jwt_token(token)
            logging.info(f'команда от: {username}')
            if username:
                logging.info(f'Command received: {command} from {username}')
                # Отправляем команду подключенному дрону
                drone_ws = connected_drones.get(username)
                logging.info(f'Drone: {drone_ws}')
                if drone_ws:
                    await drone_ws.send(f"COMMAND:{command}")
                    await websocket.send(f"AUTHORIZED: Команда {command} отправлена на дрон {username}")
                else:
                    await websocket.send(f"ERROR: Дрон {username} не подключен")
            else:
                await websocket.send("ERROR: Неверный или просроченный токен")

        else:
            await websocket.send("ERROR: Неверная команда")

# Запуск сервера WebSocket
print("Starting WebSocket server...")
start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
