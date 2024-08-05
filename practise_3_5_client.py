import requests

BASE_URL = 'http://localhost:5000/drones'


def takeoff(drone_id, altitude):
    url = f"{BASE_URL}/{drone_id}/takeoff"
    payload = {'altitude': altitude}
    response = requests.post(url, json=payload)
    return response.json()


if __name__ == '__main__':
    drone_id = "drone1"
    altitude = 200

    response = takeoff(drone_id, altitude)
    print(f"Takeoff success: {response.get('message')}")