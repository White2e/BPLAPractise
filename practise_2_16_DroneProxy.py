import jwt
import practise_2_15_srv
import time


SECRET_KEY = 'my_KEY'
SECRET_KEY_PART_1 = 'my_'
SECRET_KEY_PART_2 = 'KEY'


def get_secret_key() -> str:
    return SECRET_KEY_PART_1+SECRET_KEY_PART_2

class Drone:
    def fly(self):
        print("Drone is flying")

    def land(self):
        print("Drone is landing")

    def takeoff(self):
        print("Drone is taking off")


class DroneProxy:
    def __init__(self, drone: Drone, token: str):
        self._drone = drone
        self._token = None

    def verify_token(self):
        try:
            payload = jwt.decode(self._token, get_secret_key(), algorithms=['HS256'])
            return payload['user_id']
        except jwt.InvalidTokenError:
            print('Invalid token')
            return None
        except jwt.ExpiredSignatureError:
            print('Expired token')
            return None

    def takeoff(self):
        if self.verify_token():
            self._drone.takeoff()
        else:
            print('Access denied')

    def land(self):
        if self.verify_token():
            self._drone.land()
        else:
            print('Access denied')


def request_token(user_id):
    return practise_2_15_srv.create_token(user_id)


user_id = 123
token = request_token(user_id)
print(f'Token: {token}')

drone = Drone()
proxy = DroneProxy(drone, token)
proxy.takeoff()
proxy.land()

