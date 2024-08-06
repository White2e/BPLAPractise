import requests
from pprint import pprint


BASE_URL = 'http://localhost:5000'


# Постановка задачи БПЛА
def send_mission_to_drone(mission_id, drone_id):
    url = f"{BASE_URL}/missions/{mission_id}/{drone_id}/send"
    response = requests.post(url)
    return response.json()


# Получение списка всех БПЛА (HTTP метод: GET, Эндпоинт: `/drones`).
def get_drones():
    url = f"{BASE_URL}/drones"
    response = requests.get(url)
    return response.json()


# Получение информации о дроне (HTTP метод: GET, Эндпоинт: `/drones/{drone_id}`)



# Создание новой миссии
def create_mission(data):
    url = f"{BASE_URL}/missions"
    payload = {
      **data
    }
    response = requests.post(url, json=payload)
    return response.json()


def main():
    # Создание новой миссии
    data = {
        "id": "M001",
        "name": "Перевозка груза",
        "start_time": "2024-08-08 09:00",
        "end_time": "2024-08-08 12:00",
        "route": [
            {"latitude": 50.45, "longitude": 30.52, "altitude": 100},
            {"latitude": 50.47, "longitude": 30.55, "altitude": 200},
            {"latitude": 50.49, "longitude": 30.58, "altitude": 300}
        ]
    }
    create_mission(data)
    print(f"Миссия: {data['id']} {data['name']} создана")

    # Получение списка всех БПЛА (HTTP метод: GET, Эндпоинт: `/drones`).
    drones = get_drones()
    pprint(drones)

    # Передача миссии БПЛА дрону
    # mission_id - идентификатор миссии
    # drone_id - идентификатор дрона
    # send_mission_to_drone(mission_id, drone_id)
    drone_id = "B001"
    mission_id = "M001"
    response = send_mission_to_drone(mission_id, drone_id)
    print(f"success: {response.get('message')}")


if __name__ == '__main__':
    main()
