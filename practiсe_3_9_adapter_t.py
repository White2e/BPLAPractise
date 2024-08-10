import requests
from abc import ABC, abstractmethod


class DroneAdapter(ABC):
    @abstractmethod
    def __init__(self, base_url):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def takeoff(self):
        pass

    @abstractmethod
    def turn(self, degree):
        pass


class DroneAdapterNodejs(DroneAdapter):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_time(self):
        try:
            response = requests.get(f"{self.base_url}/time")
            response.raise_for_status()
            data = response.json()
            return data["time"]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении времени: {e}")

    def takeoff(self, drone_id):
        try:
            response = requests.get(f"{self.base_url}/{drone_id}/takeoff")
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Ошибка взлета: {e}")

    def turn(self, degree):
        pass


if __name__ == '__main__':
    # Определяем базовый URL для взаимодействия с сервером дронов
    BASE_URL = 'http://localhost:3000'

    nodejs = DroneAdapterNodejs(BASE_URL)
    print(nodejs.get_time())
    print(nodejs.takeoff(drone_id="1"))