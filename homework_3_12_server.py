#  импортируем библиотеки
from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps
from pydantic import BaseModel, ValidationError

#  наше приложение
app = Flask(__name__)

# Секретный ключ для подписи JWT токенов
app.config['SECRET_KEY'] = 'my_secret_key'

# Модель данных для аутентификации, Педантик нам будет сам генерировать исключения
class UserCredentials(BaseModel):
    username: str
    password: str

# Модель данных для команды беспилотника
class DroneCommand(BaseModel):
    action: str
    parameters: dict

# Словарь пользователей (в простом виде, в реальных приложениях будем использовать базу данных)
users = {
    'zubkov': 'pass123'
}

# Определяем декоратор для проверки JWT токена
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-tokens')

        if not token:
            return jsonify({'message': 'Токен не определен'}), 403
        #  закроем потенциально опасный код
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except Exception as e:
            return jsonify({'message': 'Токен неверен'}), 403

        return f(current_user, *args, **kwargs)

    return decorated

# Эндпоинт для аутентификации
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    try:
        credentials = UserCredentials(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    if credentials.username in users and users[credentials.username] == credentials.password:
        token = jwt.encode({
            'username': credentials.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})

    return jsonify({'message': 'Неверные данные'}), 401

# Эндпоинт для выполнения команд беспилотника, закрываем его проверкой токена
@app.route('/drone/command', methods=['POST'])
@token_required
def execute_command(current_user):
    data = request.get_json()

    try:
        command = DroneCommand(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    # Здесь должна быть логика отправки команды беспилотнику
    try:
        # Пример обработки команды (пока просто возвращаем что команда принята)
        return jsonify({'message': f'Команда {command.action} выполнена успешно: {command.parameters}'}), 200
    except Exception as e:
        return jsonify({'message': f'Ошибка выполнения команды: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
