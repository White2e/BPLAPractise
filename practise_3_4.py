from flask import Flask, Response, request, jsonify
# import cv2
# import numpy as np
# import time


# GET
#  /drones
#  /drones/{drone_id}


# POST
# /drones


# PUT
# /drones/{drone_id}


# DELETE
# /drones/{drone_id}


# Управление полетом дрона

# POST
# /drones/{drone_id}/takeoff
# /drones/{drone_id}/land
# /drones/{drone_id}/move/{x}/{y}/{z}

# GET
# /drones/{drone_id}/sensors

# Пример взлет
# POST /drones/{drone_id}/takeoff
# {
#  "altitude": 10
# }

app = Flask(__name__)

drones = {
    1: {
        "id": 1,
        "status": "landed",
        "sensors": {
            "altitude": 25,
            "latitude": 50,
            "longitude": 30,
            "battery": 100
        }
    }
}


@app.route("/drones", methods=["GET"])
def get_drones():
    return jsonify(drones), 200


@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    drone = drones.get(drone_id)
    if drone:
        return jsonify(drone), 200
    else:
        return jsonify({"message": "Drone not found"}), 404


@app.route("/drones", methods=["POST"])
def create_drone():
    drone_id = request.json.get("drone_id")
    if drone_id:
        drones[drone_id] = request.json
        return jsonify({"message": f"Drone with this id: {drone_id} added"}), 201
    else:
        return jsonify({"message": "Drone id is required"}), 404


def main():
    pass


if __name__ == '__main__':
    main()

