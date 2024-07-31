from flask import Flask, request, jsonify
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

drone_state = {
    "status": "landed",
    "battery": 100,
    "position": {
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0
    }
}

@app.route("/drone/takeoff", methods=["POST"])
def takeoff():
    try:
        global drone_state
        if drone_state["status"] == "landed" and drone_state["battery"] > 10:
            drone_state["status"] = "flying"
            drone_state["battery"] -= 10
            drone_state["position"]["altitude"] += 10
            app.logger.info("Drone is taking off")
            logging.info("Drone is taking off")
            return jsonify({
                "message": "Drone is taking off",
                "drone_state": drone_state
            }), 200
        else:
            return jsonify({"message": "Drone cannot take off"}), 400
    except Exception as e:
        app.logger.error(f"Error taking off: {str(e)}")
        return jsonify({"message": "An error occurred"}), 500


if __name__ == "__main__":
    app.run(debug=True)
