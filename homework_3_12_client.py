import requests

# URL сервера
SERVER_URL = 'http://127.0.0.1:5000'

# Данные для аутентификации
login_data = {
    'username': 'zubkov',
    'password': 'pass123'
}

# Аутентификация
response = requests.post(f'{SERVER_URL}/login', json=login_data)

if response.status_code == 200:
    token = response.json()['token']
    print(f'Успешная авторизация. Token: {token}')
else:
    print(f'Ошибка авторизации: {response.text}')
    exit(1)

# Заголовок с токеном
headers = {
    'x-access-tokens': token
}

# Команда беспилотнику
command_data = {
    'action': 'takeoff',
    'parameters': {
        'altitude': 100
    }
}

# Отправка команды
response = requests.post(f'{SERVER_URL}/drone/command', json=command_data, headers=headers)

if response.status_code == 200:
    print(f'Команда выполнена успешно: {response.json()}')
else:
    print(f'Ошибка выполнения команды: {response.text}')
