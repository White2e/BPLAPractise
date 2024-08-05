from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)
BASE_URL = "http://localhost:5000/drones"
drone = {
    "drone_index": {
        "model": "Drone 1",
        "battery": 100,
        "control_url": "http://localhost:8080"
    }
}


def set_drone(drone_id, drone_info):
    url = BASE_URL
    payload = {"drone_id": drone_id, **drone_info}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": f"Drone {drone_id} not found"}


@app.route("/takeoff", methods=["POST"])
def takeoff():
    altitude = request.json.get("altitude")
    # Логика взлета
    print(f"Взлетаем на высоту: {altitude} метров")
    return jsonify({"message": f"Взлет на высоту {altitude} выполнен"}), 200



def register_drone(drone_id, drone_info):
    url = BASE_URL
    payload = {
        "drone_id": drone_id,
        **drone_info
    }
    response = requests.post(url, json=payload)
    return response.json()




if __name__ == "__main__":
    drone_id = "drone1"
    drone_info = {
        "model": "Drone 1",
        "battery": 100,
        "control_url": "http://localhost:8080"
        }
    response = register_drone(drone_id, drone_info)
    print(f"Drone registered: {response.get('message')} \n{response}")
    app.run(host='0.0.0.0', port=8080, debug=True)

