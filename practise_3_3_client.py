import requests, cv2, json, time


base_url = "http://localhost:5000"

# Запрос на взлет
response = requests.post(f"{base_url}/drone/takeoff")
print(f"Status code: {response.status_code}")
print(response.json())


def send_telemetry_data(latitude, longitude, altitude):
    json_data = {
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude
    }
    response = requests.post(f"{base_url}/drone/telemetry", json=json_data)

    print(f"Status code: {response.status_code}, JSON: {response.json()}")


def send_video(video_frame):
    _, jpeg = cv2.imencode('.jpg', video_frame,)
    response = requests.post(f"{base_url}/drone/video", data=jpeg.tobytes())
    if response.status_code == 204:
        print("Video отправлен")
    else:
        print(f"Error. Status code: {response.status_code}")


def takeoff():
    response = requests.post(f"{base_url}/drone/takeoff")
    print(f"Status code: {response.status_code}")
    print(f"Takeoff: {response.json()}")


def update_position(latitude, longitude, altitude):
    json_data = {
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude
    }
    response = requests.put(f"{base_url}/drone/update_position", json=json_data)
    print(f"Status code: {response.status_code}, JSON: {response.json()}")



def land():
    response = requests.post(f"{base_url}/drone/land")
    print(f"Status code: {response.status_code}")
    print(f"Land: {response.json()}")


def main2():
    send_telemetry_data(55.7522200, 37.6155, 100)
    cap = cv2.VideoCapture(0)
    fps = 60
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error. Unable to read frame.")
            break
        send_video(frame)
        time.sleep(1 / fps)
    cap.release()
    print("Video capture finished.")
    cv2.destroyAllWindows()


def main():
    takeoff()
    time.sleep(1)
    update_position(55.7522200, 37.6155, 150)
    time.sleep(1)
    update_position(66.1322200, 40.3955, 100)
    time.sleep(1)
    land()


if __name__ == "__main__":
    main()

