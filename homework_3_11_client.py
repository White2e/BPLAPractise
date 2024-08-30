python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate

pip install Flask Flask-JWT-Extended



from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

users = {
    "test_user": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username not in users or users[username] != password:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

if __name__ == '__main__':
    app.run(port=5000)


Шаг 3: Реализация endpoint'ов для управления беспилотником на Python
Добавление endpoint'ов для управления беспилотником:

В app.py добавьте маршруты для управления дроном. Эти маршруты будут защищены JWT токенами:

@app.route('/drone', methods=['POST'])
@jwt_required()
def control_drone():
    data = request.json
    # Предполагаем, что у вас есть функция для отправки команд дрону
    response = send_drone_command(data)
    return jsonify(response)


Реализация функций для взаимодействия с API беспилотника:

Опишите функции, которые будут отправлять команды в API дрон

def send_drone_command(data):
    # Пример отправки данных в API дрона
    # Здесь используйте реальный API беспилотника
    response = {"status": "command received", "data": data}
    return response

Запуск проекта
Запуск Flask API:

Запустите Python сервер:
bash
Копировать код
python app.py
Запуск Node.js сервера:

Запустите Node.js сервер:
bash
Копировать код
node server.js
Теперь у вас есть работающий сервер на Node.js, который оборачивает API, реализованный на Python. Этот API управляет дроном и защищен авторизацией JWT.







import requests


def get_time(format='iso'):
    url = 'http://localhost:3000/time'
    params = {'format': format}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Current time (format: {format}): {data['time']}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    get_time('iso')  # Получение времени в формате ISO
    get_time('utc')  # Получение времени в формате UTC
    get_time('locale')  # Получение времени в локальном формате
