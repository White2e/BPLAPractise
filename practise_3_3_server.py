from flask import Flask, request, jsonify, Response
import cv2
import numpy as np
import time
import logging


app = Flask(__name__)

drone_state = {
    "status": "landed",
    "battery": 100,
    "position": {
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0
    },
     "telemetry_data": []
}


video_frame = None
fps = 10
quality = 80

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



@app.route("/drone/land", methods=["POST"])
def land():
    try:
        global drone_state
        if drone_state["status"] != "landed":
            drone_state["status"] = "landed"
            drone_state["battery"] -= 10
            drone_state["position"]["altitude"] -= 10
            app.logger.info("Drone is landing")
            logging.info("Drone is landing")
            return jsonify({
                "message": "Drone is landing",
                "drone_state": drone_state
            }), 200
        else:
            return jsonify({"message": "Drone cannot landing"}), 400
    except Exception as e:
        app.logger.error(f"Error landing: {str(e)}")
        return jsonify({"message": "An error occurred"}), 500


@app.route("/drone/update_position", methods=["POST", "PUT"])
def update_position():
    data = request.json
    if "latitude" in data and "longitude" in data and "altitude" in data:
        if request.method == "PUT":
            drone_state["position"]["latitude"] = data["latitude"]
            drone_state["position"]["longitude"] = data["longitude"]
            drone_state["position"]["altitude"] = data["altitude"]
            app.logger.info("Drone position updated")
            logging.info("Drone position updated")
            return jsonify({
                "message": "Drone position updated",
                "drone_state": drone_state
            }), 200
    else:
        return jsonify({"message": "Invalid position data"}), 400



@app.route("/drone/telemetry", methods=["POST"])
def receive_telemetry():
    data = request.json
    drone_state["telemetry_data"].append(data)
    return jsonify({"status": "Получили"}), 200


@app.route("/drone/display", methods=["GET"])
def display_telemetry():
    return jsonify({"telemetry_data": drone_state["telemetry_data"]}), 200


@app.route("/drone/video", methods=["POST"])
def receive_video():
    global video_frame
    np_array = np.frombuffer(request.data, dtype=np.uint8)
    video_frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return jsonify({"message": "Video received"}), 204


@app.route("/drone/video_feed")
def video_feed():
    def generate():
        global video_frame
        while True:
            if video_frame is not None:
                _, jpeg = cv2.imencode('.jpg', video_frame, [int(cv2.IMWRITE_JPEG_QUALITY), quality]) # 8
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(1 / fps)
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')



def main():
    app.run(host='0.0.0.0', port=5000, debug=True)



if __name__ == "__main__":
    main()
