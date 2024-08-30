import requests

# Определяем базовый URL для взаимодействия с сервером дронов
BASE_URL = 'http://localhost:3000'


def send_command(command, format_time: None):
    params = {'format': format_time}
    try:
        # Получаем текущую дату и время с сервера
        res_date = requests.get(f"{BASE_URL}/time", params=params)
        data = res_date.json()
        print(f"Current server time (format: {format_time}): {data['time']}")

        # Выполняем указанную команду на сервере дрона
        url = f"{BASE_URL}/{command}"
        response = requests.get(url, None)
        # Отображаем результат выполнения команды на сервере дрона
        if response.status_code == 200:
            data = response.json()
            print("The command was executed successfully.: ", data['message'])
        else:
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(e)


def login(username, password, command):
    response = requests.post(f"{BASE_URL}/drone-control", json={'username': username, 'password': password, 'command': command, 'token': '', 'status': ''})
    data = response.json()
    print(response.json(), response.status_code)
    if (response.status_code == 200) and (data['token']):
        print(f"Пользователь {username} авторизован.")
        return response.json().get('token')
    elif response.status_code == 403:
        print(f"Пользователь {username} не авторизован.")
    else:
        print(f"Ошибка авторизации.")
    return None


def register(username, password, command):
    response = requests.post(f"{BASE_URL}/drone-control", json={'username': username, 'password': password, 'command': command, 'token': '', 'status': ''})
    if response.status_code == 201:
        print(f"Пользователь {username} зарегистрирован.")
    elif response.status_code == 400:
        print(f"Пользователь {username} уже зарегистрирован.")


if __name__ == '__main__':
    register('admin', 'pass123', 'register')
    login('admin', 'pass123', 'login')
    send_command("drone1/takeoff", 'local')
    send_command("drone1/land", 'local')

