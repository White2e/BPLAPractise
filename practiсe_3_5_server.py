from flask import Flask, Response, request, jsonify
import requests

# Управление дронами

# GET
# /drones
# /drones/{drone_id}

# POST
# /drones

# PUT
# /drones/{drone_id}

# DELETE
# /drones/{drone_id}


# Управление полетом

# POST
# /drones/{drone_id}/takeoff
# /drones/{drone_id}/land
# /drones/{drone_id}/move

# GET
# /drones/{drone_id}/sensors

# Пример взлет
# POST /drones/{drone_id}/takeoff
# {
#     "altitude": 10
# }

app = Flask(__name__)

drones = {}


@app.route("/drones", methods=["GET"])
def get_drones():
    return jsonify(drones), 200


@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    drone = drones.get(drone_id)
    if drone:
        return jsonify(drone), 200
    return jsonify({"error": "Дрон не найден"}), 404


@app.route("/drones", methods=["POST"])
def create_drone():
    drone_id = request.json.get("drone_id")
    if drone_id:
        drones[drone_id] = request.json
        return jsonify({"message": f"Дрон {drone_id} добавлен"}), 201
    return jsonify({"error": "Не передан id дрона"}), 404


@app.route("/drones/<drone_id>/takeoff", methods=["POST"])
def takeoff_drone(drone_id):
    if drone_id in drones:
        altitude = request.json.get("altitude")
        drone_info = drones[drone_id]
        drone_url = drone_info["control_url"] + "/takeoff"
        response = requests.post(drone_url, json={"altitude": altitude})
        if response.status_code == 200:
            return jsonify({"message": f"Дрон {drone_id} взлетел на высоту {altitude}\n{response.json().get('message')}"}), 200
        else:
            return jsonify({"error": f"Ошибка взлета {drone_id}"}), 500

        return jsonify({"message": f"Дрон {drone_id} взлетел"})
    else:
        return jsonify({"error": f"Дрон {drone_id} не зарегистрирован"}), 404

if __name__ == '__main__':
    app.run(debug=True)
