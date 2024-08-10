import requests
from abc import ABC, abstractmethod


# Определяем базовый URL
BASE_URL = "http://localhost:3000"

class DroneAdapter(ABC):
    @abstractmethod
    def __init__(self, base_url):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def get_takeoff(self):
        pass

    @abstractmethod
    def turn(self, degree):
        pass

class DroneAdapterNodejs(DroneAdapter):
    def __init__(self, base_url):
        self._base_url = base_url
        #super().__init__(base_url)

    def get_time(self):
        response = requests.get(f"{self._base_url}/time")
        response.raise_for_status()
        data = response.json()
        return data["time"]

    def takeoff(self, drone_id):
        response = requests.get(f"{self._base_url}/{drone_id}/takeoff")
        response.raise_for_status()
        data = response.json()
        return data["status"]

def main():
    adapter = DroneAdapterNodejs(BASE_URL)
    print(adapter.get_time())
    print(adapter.takeoff(drone_id="drone1"))


if __name__ == "__main__":
    main()
