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


# Получение списка всех миссий (HTTP метод: GET, Эндпоинт: `/missions`)
def get_missions():
    url = f"{BASE_URL}/missions"
    response = requests.get(url)
    return response.json()


# Получение информации о конкретной миссии (HTTP метод: GET, Эндпоинт: `/missions/{id}`)
def get_mission(id):
    url = f"{BASE_URL}/missions/{id}"
    response = requests.get(url)
    return response.json()

# Получение информации о дроне (HTTP метод: GET, Эндпоинт: `/drones/{drone_id}`)
def get_drone(drone_id):
    url = f"{BASE_URL}/drones/{drone_id}"
    response = requests.get(url)
    return response.json()


#  Обновление информации о БПЛА (HTTP метод: PUT, Эндпоинт: `/drones/{id}
def update_drone(drone_id, data):
    url = f"{BASE_URL}/drones/{drone_id}"
    payload = {
        **data
    }
    response = requests.put(url, json=payload)
    return response.json()


# Обновление информации о миссии (HTTP метод: PUT, Эндпоинт: `/missions/{id}`)
def update_mission(id, data):
    url = f"{BASE_URL}/missions/{id}"
    payload = {
        **data
    }
    response = requests.put(url, json=payload)
    return response.json()


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
    print("")
    data = {
        "id": "M002",
        "name": "Патрулирование",
        "start_time": "2024-08-08 02:00",
        "end_time": "2024-08-08 10:00",
        "route": [
            {"latitude": 51.45, "longitude": 30.52, "altitude": 100},
            {"latitude": 51.47, "longitude": 30.55, "altitude": 200},
            {"latitude": 51.49, "longitude": 30.58, "altitude": 300}
        ]
    }
    create_mission(data)
    print(f"Миссия: {data['id']} {data['name']} создана")
    print("")

    # Получение списка всех БПЛА
    print("Request info on all active UAVs")
    drones = get_drones()
    pprint(drones)
    print("")

    # Получение информации о конкретном БПЛА
    drone_id = "B001"
    print(f"Request info on Drone ID: {drone_id}...")
    drones = get_drone(drone_id)
    pprint(drones)
    print("")

    # Получение списка всех миссий
    print("Request info on all missions")
    missions = get_missions()
    pprint(missions)
    print("")

    # Получение информации о конкретной миссии
    mission_id = "M001"
    print(f"Request info on Mission ID: {mission_id}...")
    mission = get_mission(mission_id)
    pprint(mission)
    print("")

    # Передача миссии БПЛА дрону
    # mission_id - идентификатор миссии
    # drone_id - идентификатор дрона
    # send_mission_to_drone(mission_id, drone_id)
    print("Send mission to Drone ...")
    drone_id = "B001"
    mission_id = "M001"
    response = send_mission_to_drone(mission_id, drone_id)
    print(f"success: {response.get('message')}")
    print("")

    #  Обновление информации о БПЛА (HTTP метод: PUT, Эндпоинт: `/drones/{id}
    drone_id = "B001"
    payload = {
        "name": "Autel Robotics EVO MAX4N s.v.Defender",
        "status": "landed"
    }
    print(f"Update info on Drone ID: {drone_id}...")
    drones = update_drone(drone_id, payload)
    print(f"success: {response.get('message')}")
    print("")

    # Обновление информации о миссии
    mission_id = "M001"
    payload = {
        "name": "Перевозка груза (новое название)",
        "start_time": "2024-08-08 10:00",
        "end_time": "2024-08-08 11:00"
    }
    print(f"Update info on Mission ID: {mission_id}...")
    missions = update_mission(mission_id, payload)
    print(f"success: {response.get('message')}")
    print("")

    # Удаление миссии
    mission_id = "M001"
    print(f"Delete Mission ID: {mission_id}...")
    response = requests.delete(f"{BASE_URL}/missions/{mission_id}")
    print(f"success: {response.status_code == 200}")
    print("")


if __name__ == '__main__':
    main()
