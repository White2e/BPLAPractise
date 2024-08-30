import requests


def get_time():
    url = 'http://localhost:3000/time'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Current time: {data['time']}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    get_time()  # Получение времени в локальном формате
