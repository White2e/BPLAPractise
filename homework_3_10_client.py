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
