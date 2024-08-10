import requests


# Определяем базовый URL
BASE_URL = "http://localhost:3000"

def send_command(command):
    try:
        response = requests.get(f'{BASE_URL}/{command}')
        if response.status_code == 200:
            data = response.json()
            print("Server data: ", data)
        else:
            print("Error: ", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error occurred: ", e)



# Точка входа в приложение
if __name__ == "__main__":
    send_command("time")
    send_command("1/takeoff")
