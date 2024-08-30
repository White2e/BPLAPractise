#  homework_2_2_1 - итератор - управление роем дронов
#  homework_2_7 - работа с базой данных
#  homework_2_8 - секьюри - прокси
#  homework_3_9_client - управление дроном
#  homework_3_9_drone_1 - дрон
#  homework_3_9_server - сервер
#  homework_3_10_server - сервер на ноде джи эс
#  homework_3_12_server - авторизация JWT
#  practise_1_4 - класс дрона
#  practise_1_5 - класс гпс
#  practise_1_7 - движение дрона по маршруту
#  practise_1_11 - рисование маршрута дрона
#  practise_2_1_1 - фабричный метод
#  practise_2_4 - нотифай декоратор
#  practise_2_6 - наблюдатель
#  practise_2_7 - команда
#  practise_2_11 - абстрактная фабрика и строитель
#  practise_3_2_client - обмен телеметрией, работа с камерой
#  practise_3_3_client - обмен телеметрией, работа с камерой
#  practise_3_6_client - web-форма управления
#  practise_3_6_drone_server - сервер с веб сокетами
#  practise_3_7_drone_server - сервер с веб сокетами
#  practise_3_8_server - сервер на ноде
#  practise_3_9_adapter - адаптер к серверу
#  practise_3_12 - дроне апи фактори
#  practise_3_13 - стратегии
#  practise_4_4 - в нескольких потоках с аирсим и профилированием

"""
Объяснение кода сервера
Секретный ключ (SECRET_KEY) используется для подписи и проверки JWT-токенов. Этот ключ должен быть достаточно сложным и храниться в секрете.

users_db — простая база данных пользователей, где ключом является имя пользователя, а значением — пароль. В реальном приложении это будет база данных.

create_jwt_token(username) — функция, которая создает JWT-токен с полезной нагрузкой, содержащей имя пользователя, время создания и время истечения токена.

verify_jwt_token(token) — функция для проверки JWT-токена. Если токен действителен, возвращается имя пользователя, иначе возвращается None.

handle_client(websocket, path) — функция, обрабатывающая входящие сообщения от клиентов:

Если сообщение начинается с "LOGIN:", сервер ожидает получение логина и пароля, которые затем проверяются. Если они правильные, сервер возвращает JWT-токен.
В остальных случаях сервер ожидает JWT-токен и проверяет его. Если токен действителен, сервер принимает команду и подтверждает это клиенту.
Запуск сервера — сервер запускается и начинает прослушивать соединения на порту 8765.

Как это работает:
Клиент отправляет сообщение вида LOGIN:username,password.
Если авторизация успешна, сервер возвращает клиенту JWT-токен.
Клиент может использовать этот токен для последующих команд, отправляя его серверу, который проверяет токен и выполняет команду.
Важно:
В реальных проектах данные должны передаваться по защищенному каналу (например, через WSS — WebSocket Secure).
Не храните пароли в открытом виде в localStorage, это лишь учебный пример.
JWT-токены следует защищать от утечек и перехвата.




Объяснение кода клиента:
HTML и CSS: Создается простая форма авторизации с полями для ввода имени пользователя и пароля, а также кнопкой для входа.

WebSocket соединение:

Функция connectSocket() устанавливает соединение с WebSocket-сервером по адресу ws://localhost:8765.
При успешном соединении (onopen) выводится сообщение в консоль.
При получении сообщения от сервера (onmessage):
Если сообщение начинается с "JWT:", это означает, что сервер вернул JWT-токен, который сохраняется в localStorage.
В случае ошибки или другого сообщения выводится соответствующее уведомление в элемент с id="statusMessage".
Ошибки соединения обрабатываются в onerror.
Функция login():

Берет значение из полей ввода имени пользователя и пароля.
Проверяет, установлено ли соединение с сервером. Если нет, оно устанавливается.
Отправляет серверу строку вида LOGIN:username,password.
Автоматическое подключение:

При загрузке страницы сразу устанавливается соединение с WebSocket-сервером.
Использование:
Пользователь вводит свои учетные данные и нажимает кнопку "Войти".
Если авторизация проходит успешно, пользователь получает JWT-токен, который сохраняется в localStorage.
Токен можно использовать для последующих запросов к серверу через WebSocket.
Этот код является учебным примером, и в реальных приложениях следует уделять больше внимания безопасности, например, защищать соединения с помощью WSS и избегать хранения пароля в открытом виде.

----

Объяснение кода:
Добавлена новая форма для управления дроном:

command-container — это новый блок, который становится видимым только после успешной авторизации.
Поле ввода для команды (<input type="text" id="command" placeholder="Введите команду">).
Кнопка для отправки команды (<button onclick="sendCommand()">Отправить команду</button>).
Поле для отображения ответа сервера (<p class="server-response" id="serverResponse"></p>).
Функция sendCommand():

Получает введенную команду и токен из localStorage.
Формирует сообщение в формате COMMAND:, JWT-токен, команда.
Отправляет это сообщение на сервер через WebSocket.
Обработка ответа сервера:

Если сервер отправляет сообщение, начинающееся с "AUTHORIZED:", оно выводится в элемент serverResponse с зелёным цветом.
Если сервер отправляет JWT-токен после успешной авторизации, форма управления дроном становится видимой.
Автоматическое подключение:

При загрузке страницы сразу устанавливается соединение с WebSocket-сервером.
Использование:
Пользователь вводит свои учетные данные и нажимает "Войти".
После успешной авторизации появляется форма для отправки команд дрону.
Вводится команда и отправляется на сервер, который возвращает результат, отображаемый под формой команд.

---


Объяснение изменений:
Размеры контейнеров:

Ширина контейнеров уменьшена до 250px, что делает форму компактнее.
Padding уменьшен до 15px.
Поле ввода и кнопки:

Уменьшен padding внутри полей ввода и кнопок до 8px.
Размер шрифта уменьшен до 14px.
Отступы и текст:

Уменьшены отступы между элементами формы.
Заголовки (<h2>) уменьшены до 18px, что визуально уменьшает форму.
Сокращение вертикальных отступов:

Поля ввода и кнопки теперь с меньшими вертикальными отступами и отступами снизу, что экономит место.
Результат:
Форма стала более компактной, не теряя при этом своей функциональности и удобства. Она по-прежнему сохраняет читабельность и функциональность, но занимает меньше места на экране.


"""

"""
Для того чтобы реализовать клиент на WebSocket, который подключается к серверу и выполняет авторизацию с использованием JWT-токенов, а также принимает и выполняет команды от сервера, нам нужно объединить функциональность работы с WebSocket и JWT.

Шаг 1: Модификация WebSocket клиента
Мы создадим клиента, который будет:

Подключаться к серверу WebSocket.
Отправлять JWT-токен для авторизации.
Принимать и обрабатывать команды от сервера.
Код WebSocket клиента
"""
import asyncio
import websockets
import jwt

# Конфигурация
SERVER_URL = "ws://localhost:8765"  # Адрес WebSocket сервера
SECRET_KEY = 'your_secret_key_here'  # Секретный ключ, используемый для создания JWT токенов
USERNAME = 'admin'
PASSWORD = 'password123'


# Функция для создания JWT токена
def create_jwt_token(username, secret_key):
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, secret_key, algorithm="HS256")
    return token


async def websocket_client():
    token = create_jwt_token(USERNAME, SECRET_KEY)

    async with websockets.connect(SERVER_URL) as websocket:
        # Отправка токена серверу для авторизации
        auth_message = {'type': 'auth', 'token': token}
        await websocket.send(str(auth_message))
        print(f"Sent to server: {auth_message}")

        # Ожидание ответа от сервера на авторизацию
        auth_response = await websocket.recv()
        print(f"Received from server: {auth_response}")

        if auth_response == "Authorization successful":
            print("Authorization successful. Waiting for commands...")
            while True:
                # Получение команды от сервера
                command_message = await websocket.recv()
                print(f"Received command: {command_message}")

                # Обработка команды (например, просто распечатаем)
                # В реальном приложении здесь может быть логика управления дроном
                response = f"Command {command_message} received and executed."
                await websocket.send(response)
                print(f"Sent to server: {response}")
        else:
            print("Authorization failed.")


# Запуск клиента
asyncio.get_event_loop().run_until_complete(websocket_client())

"""
Шаг 2: Модификация WebSocket сервера
Теперь давайте создадим сервер, который будет проверять JWT токены от клиента и отправлять команды, если авторизация успешна.

Код WebSocket сервера

"""
import asyncio
import websockets
import jwt
import datetime

SECRET_KEY = 'your_secret_key_here'  # Секретный ключ, используемый для проверки JWT токенов


# Функция для проверки JWT токена
def verify_jwt_token(token, secret_key):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded['username']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


async def websocket_server(websocket, path):
    try:
        # Получаем сообщение от клиента
        auth_message = await websocket.recv()
        print(f"Received from client: {auth_message}")

        # Здесь предполагается, что сообщение это словарь, переданный как строка
        auth_data = eval(auth_message)

        if auth_data['type'] == 'auth' and 'token' in auth_data:
            username = verify_jwt_token(auth_data['token'], SECRET_KEY)
            if username:
                await websocket.send("Authorization successful")
                print(f"User {username} authorized.")

                # Отправляем команду после авторизации
                while True:
                    # Например, сервер может отправить команду "takeoff"
                    command = "takeoff"
                    await websocket.send(command)
                    print(f"Sent command to client: {command}")

                    # Ожидание ответа от клиента
                    response = await websocket.recv()
                    print(f"Received from client: {response}")

                    # Задержка перед отправкой следующей команды
                    await asyncio.sleep(5)
            else:
                await websocket.send("Authorization failed")
                print("Authorization failed")
        else:
            await websocket.send("Invalid request")
            print("Invalid request received")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close()


# Запуск сервера на порту 8765
start_server = websockets.serve(websocket_server, "localhost", 8765)

# Запуск события в асинхронном цикле
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

"""
Как это работает:
Клиент:

Генерирует JWT-токен на основе username и SECRET_KEY.
Подключается к серверу WebSocket и отправляет токен для авторизации.
После успешной авторизации клиент принимает команды от сервера и выполняет их (в данном случае просто отправляет подтверждение обратно серверу).
Сервер:

Ожидает подключения клиента и принимает JWT-токен.
Проверяет токен с использованием SECRET_KEY.
Если токен валиден, сервер отправляет команды клиенту, которые тот должен выполнить.

Запуск:
Сначала запустите WebSocket сервер:

bash
Копировать код
python websocket_server.py
Затем запустите WebSocket клиента:

bash
Копировать код
python websocket_client.py
Вы увидите, как клиент подключается к серверу, проходит авторизацию и начинает получать команды от сервера.



Для того чтобы клиент (дрон) поддерживал постоянное WebSocket-соединение для получения команд от сервера, необходимо модифицировать код клиента. Основная идея состоит в том, чтобы клиент, после успешной авторизации, оставался подключенным к серверу и постоянно слушал команды, которые сервер отправляет.

Обновленный код клиента

"""

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
            token = auth_response[4:]
            logging.info("Authorization successful. Waiting for commands...")

            while True:
                try:
                    # Ожидание команды от сервера
                    command_message = await websocket.recv()
                    logging.info(f"Received command: {command_message}")

                    if command_message == "takeoff":
                        response = "Drone is taking off"
                        logging.info(response)
                    elif command_message == "land":
                        response = "Drone is landing"
                        logging.info(response)
                    else:
                        response = f"Unknown command: {command_message}"
                        logging.warning(response)

                    # Отправка ответа серверу
                    await websocket.send(f"Response: {response}")

                except websockets.ConnectionClosedError:
                    logging.error("Connection with server lost.")
                    break

        else:
            logging.error("Authorization failed.")

# Запуск клиента
asyncio.get_event_loop().run_until_complete(websocket_client())


"""
Что изменилось:
Постоянное соединение: После успешной авторизации клиент (дрон) входит в бесконечный цикл, где он ожидает команды от сервера.

Обработка команд: Клиент постоянно слушает команды от сервера (takeoff, land и т. д.) и выполняет соответствующие действия. В этом примере команды просто обрабатываются и выводятся в лог, но на практике здесь может быть вызов функций для управления дроном.

Обработка ошибок: Если соединение с сервером закрывается (например, сервер падает или происходит сбой в сети), клиент логирует ошибку и выходит из цикла.

Серверная часть
Код сервера в данном случае также остается почти таким же. Единственное, что важно - сервер должен периодически отправлять команды дрону.

Пример сервера, отправляющего команды:

"""

import asyncio
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
            else:
                await websocket.send("ERROR: Неверные имя пользователя или пароль")

        elif data.startswith("COMMAND:"):
            credentials = data[8:].split(",")
            token = credentials[0]
            command = credentials[1]

            username = verify_jwt_token(token)
            if username:
                await websocket.send(f"AUTHORIZED: Команда {command} принята от {username}")
            else:
                await websocket.send("ERROR: Неверный или просроченный токен")

        else:
            await websocket.send("ERROR: Неверная команда")


async def send_commands_to_drone(websocket, path):
    try:
        await websocket.send("takeoff")
        await asyncio.sleep(10)
        await websocket.send("land")
    except websockets.ConnectionClosedError as e:
        logging.error(f"Client disconnected: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Запуск сервера WebSocket
print("Starting WebSocket server...")
start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

"""
Запуск:
Запустите сервер. Он будет ждать подключения клиента и обрабатывать команды.
Запустите клиента (дрон). Клиент подключится к серверу, авторизуется и будет слушать команды от сервера.
Таким образом, клиент (дрон) остается подключенным к серверу и готов принимать команды в реальном времени, обеспечивая двустороннее взаимодействие через WebSocket.
"""



