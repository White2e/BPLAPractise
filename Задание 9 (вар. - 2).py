from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Пример данных
drones = []
missions = []

class Drone:
    def __init__(self, name, status, location):
        self.id = len(drones) + 1
        self.name = name
        self.status = status
        self.location = location

class Mission:
    def __init__(self, name, start_time, end_time, route):
        self.id = len(missions) + 1
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.route = route

def get_drone_by_id(id):
    return next((d for d in drones if d.id == id), None)

def get_mission_by_id(id):
    return next((m for m in missions if m.id == id), None)

# Эндпоинты для БПЛА
@app.route('/drones', methods=['POST'])
def create_drone():
    data = request.json
    if not data or 'name' not in data or 'status' not in data or 'location' not in data:
        abort(400)
    drone = Drone(data['name'], data['status'], data['location'])
    drones.append(drone)
    return jsonify(drone.__dict__), 201

@app.route('/drones', methods=['GET'])
def get_drones():
    return jsonify([drone.__dict__ for drone in drones]), 200

@app.route('/drones/<int:id>', methods=['GET'])
def get_drone(id):
    drone = get_drone_by_id(id)
    if drone:
        return jsonify(drone.__dict__), 200
    else:
        abort(404)

@app.route('/drones/<int:id>', methods=['PUT'])
def update_drone(id):
    drone = get_drone_by_id(id)
    if not drone:
        abort(404)
    data = request.json
    if not data:
        abort(400)
    drone.name = data.get('name', drone.name)
    drone.status = data.get('status', drone.status)
    drone.location = data.get('location', drone.location)
    return jsonify(drone.__dict__), 200

@app.route('/drones/<int:id>', methods=['DELETE'])
def delete_drone(id):
    global drones
    drone = get_drone_by_id(id)
    if not drone:
        abort(404)
    drones = [d for d in drones if d.id != id]
    return jsonify({'message': 'Drone deleted'}), 200

# Эндпоинты для миссий
@app.route('/missions', methods=['POST'])
def create_mission():
    data = request.json
    if not data or 'name' not in data or 'start_time' not in data or 'end_time' not in data or 'route' not in data:
        abort(400)
    mission = Mission(data['name'], data['start_time'], data['end_time'], data['route'])
    missions.append(mission)
    return jsonify(mission.__dict__), 201

@app.route('/missions', methods=['GET'])
def get_missions():
    return jsonify([mission.__dict__ for mission in missions]), 200

@app.route('/missions/<int:id>', methods=['GET'])
def get_mission(id):
    mission = get_mission_by_id(id)
    if mission:
        return jsonify(mission.__dict__), 200
    else:
        abort(404)

@app.route('/missions/<int:id>', methods=['PUT'])
def update_mission(id):
    mission = get_mission_by_id(id)
    if not mission:
        abort(404)
    data = request.json
    if not data:
        abort(400)
    mission.name = data.get('name', mission.name)
    mission.start_time = data.get('start_time', mission.start_time)
    mission.end_time = data.get('end_time', mission.end_time)
    mission.route = data.get('route', mission.route)
    return jsonify(mission.__dict__), 200

@app.route('/missions/<int:id>', methods=['DELETE'])
def delete_mission(id):
    global missions
    mission = get_mission_by_id(id)
    if not mission:
        abort(404)
    missions = [m for m in missions if m.id != id]
    return jsonify({'message': 'Mission deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
