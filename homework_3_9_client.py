import requests

BASE_URL = 'http://localhost:5000'


# Постановка задачи БПЛА
def send_mission_to_drone(mission_id, drone_id):
    url = f"{BASE_URL}/missions/{mission_id}/{drone_id}/send"
    response = requests.post(url)
    return response.json()


# Создание новой миссии
def create_mission():
    url = f"{BASE_URL}/missions"
    payload = {
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
    response = requests.post(url, json=payload)
    return response.json()


def main():
    create_mission()  # Создание новой миссии
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
