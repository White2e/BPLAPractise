from flask import Flask, Response, request, jsonify
import requests

# Конфигурация БПЛА
app = Flask(__name__)
# "БПЛА" с атрибутами `id`, `name`, `status`, `location`.
drone = {
    "id": "B001",
    "name": "Autel Robotics s.v.Defender",
    "status": "landed",
    "location": {
        "latitude": 50.45,
        "longitude": 30.52,
        "altitude": 100
    },
    "control_url": "http://localhost:8080"
}

# "Миссия" с атрибутами `id`, `name`, `start_time`, `end_time`, `route`
mission = {
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

BASE_URL = "http://localhost:5000/drones"


# Регистрация БПЛА
def register_drone():
    payload = {
        **drone
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        drone['status'] = 'active'
    return response.json()


# Получение миссии с сервера
@app.route('/missions', methods=['POST'])
def create_mission():
    print(request.json)
    mission_id = request.json.get('id')
    if mission_id:
        mission[mission_id] = request.json
        return jsonify({'message': 'Mission created on Drone'}), 201
    return jsonify({'error': 'Mission ID required'}), 400


# Взлет
@app.route("/takeoff", methods=["POST"])
def takeoff():
    altitude = request.json.get("altitude")
    # Логика взлета
    print(f"Взлетаем на высоту: {altitude} метров")
    return jsonify({"message": f"Взлет на высоту {altitude} выполнен"}), 200


# Посадка
@app.route("/land", methods=["POST"])
def land():
    altitude = request.json.get("altitude")
    # Логика посадки
    print(f"Посадка с высоты: {altitude} метров")
    return jsonify({"message": f"Посадка с высоты {altitude} выполнена"}), 200


def main():
    response = register_drone()
    print(f"БПЛА зарегистрирован для выполнения задач: {response['message']}")
    app.run(port=8080, debug=True)
    print("БПЛА выключен")


# Запуск приложения при запуске скрипта
if __name__ == "__main__":
    main()
