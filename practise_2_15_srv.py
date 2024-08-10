import jwt
import datetime

SECRET_KEY = 'my_KEY'


def create_token(user_id):
    """Создание JWT-токена с указанным идентификатором пользователя."""
    payload = {
        'exp': datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(minutes=5),
        'user_id': user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def get_token(user_id):
    """Получение JWT-токена для указанного идентификатора пользователя."""
    if user_id == 'user123':
        token = create_token(user_id)
        print(f'Токен для пользователя {user_id}: {token}')
        return token


user_id = 'user123'
token = create_token(user_id)
print(token)

# Проверка токена
decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
print(f'Декодированный токен: {decoded_token}')
