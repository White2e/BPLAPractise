# Задание - проектирование RESTful интерфейсов
from flask import Flask, Response, request, jsonify
import requests


# Приложение
app = Flask(__name__)
# "БПЛА" с атрибутами `id`, `name`, `status`, `location`
drones = {}
# "Миссия" с атрибутами `id`, `name`, `start_time`, `end_time`, `route`
missions = {}


# Получение списка всех БПЛА (HTTP метод: GET, Эндпоинт: `/drones`)
@app.route('/drones', methods=['GET'])
def get_drones():
    return jsonify(drones), 200


# Получение информации о конкретном БПЛА (HTTP метод: GET, Эндпоинт: `/drones/{id}`)
@app.route('/drones/<id>', methods=['GET'])
def get_drone(id):
    drone = drones.get(id)
    if drone:
        return jsonify(drone), 200
    return jsonify({'error': f'Drone ID:{id} not found'}), 404


#  Создание нового БПЛА (HTTP метод: POST, Эндпоинт: `/drones`)
@app.route('/drones', methods=['POST'])
def create_drone():
    id = request.json.get('id')
    if id:
        drones[id] = request.json
        drones[id]['status'] = 'active'
        return jsonify({'message': f'Drone ID:{id} created'}), 201
    return jsonify({'error': 'Drone ID required'}), 400


# Обновление информации о БПЛА (HTTP метод: PUT, Эндпоинт: `/drones/{id}
@app.route('/drones/<id>', methods=['PUT'])
def update_drone(id):
    drone = drones.get(id)
    if drone:
        drone.update(request.json)
        print(drones.get(id))
        return jsonify({'message': f'Drone ID:{id} updated'}), 200
    return jsonify({'error': f'Drone ID:{id} not found'}), 404


# Удаление БПЛА (HTTP метод: DELETE, Эндпоинт: `/drones/{id}`)
@app.route('/drones/<id>', methods=['DELETE'])
def delete_drone(id):
    if id in drones:
        del drones[id]
        return jsonify({'message': f'Drone ID:{id} deleted'}), 200
    return jsonify({'error': f'Drone ID:{id} not found'}), 404


# Создание новой миссии (HTTP метод: POST, Эндпоинт: `/missions`)
@app.route('/missions', methods=['POST'])
def create_mission():
    mission_id = request.json.get('id')
    if mission_id:
        missions[mission_id] = request.json
        return jsonify({'message': 'Mission created'}), 201
    return jsonify({'error': 'Mission ID required'}), 400


# Получение списка всех миссий (HTTP метод: GET, Эндпоинт: `/missions`)
@app.route('/missions', methods=['GET'])
def get_missions():
    return jsonify(missions), 200


# Получение информации о конкретной миссии (HTTP метод: GET, Эндпоинт: `/missions/{id}`)
@app.route('/missions/<id>', methods=['GET'])
def get_mission(id):
    mission = missions.get(id)
    if mission:
        return jsonify(mission), 200
    return jsonify({'error': f'Mission ID:{id} not found'}), 404


# Обновление информации о миссии (HTTP метод: PUT, Эндпоинт: `/missions/{id}`)
@app.route('/missions/<id>', methods=['PUT'])
def update_mission(id):
    mission = missions.get(id)
    if mission:
        mission.update(request.json)
        return jsonify({'message': f'Mission ID:{id} updated'}), 200
    return jsonify({'error': f'Mission ID:{id} not found'}), 404


# Удаление миссии (HTTP метод: DELETE, Эндпоинт: `/missions/{id}`)
@app.route('/missions/<id>', methods=['DELETE'])
def delete_mission(id):
    if id in missions:
        del missions[id]
        return jsonify({'message': f'Mission ID:{id} deleted'}), 200
    return jsonify({'error': f'Mission ID:{id} not found'}), 404


# Отправка миссии <ID> на БПЛА <ID>
@app.route('/missions/<mission_id>/<drone_id>/send', methods=['POST'])
def send_mission_to_drone(mission_id, drone_id):
    mission = missions.get(mission_id)
    if mission:
        drone = drones.get(drone_id)
        if drone:
            if drone['status'] == 'active':
                drone_url = drone['control_url']
                response = requests.post(drone_url, json=mission)
                if response.status_code == 201:
                    drones['location'] = mission['route'][0]
                    drones['status'] = 'mission'
                    print(drones)
            else:
                return jsonify({'error': 'Drone is not active'}), 400
            return jsonify({'message': f'Mission ID:{mission_id} sent to Drone ID:{drone_id}'}), 200
        return jsonify({'error': f'Drone ID:{drone_id} not found'}), 404
    return jsonify({'error': f'Mission ID:{mission_id} not found'}), 404


def main():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()
