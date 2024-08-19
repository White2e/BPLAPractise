from practise_3_13 import *
import jwt

SECRET_KEY = 'my_token'


class SafetyCheck(ICommand):
    def __init__(self, secret_key: str):
        self.__secret_key = secret_key

    def __call__(self, command: ICommand, token: str):
        self.__command = command
        self.__token = token
        return self


    def execute(self):
        # Check
        if self.check_token():
            self.__command.execute()
        else:
            print("Safety check failed")

    def check_token(self):
        print("Safety check...")
        # logic
        try:
            decode_token = jwt.decode(self.__token, self.__secret_key, algorithms=['HS256'])
            print(f"Decoded token: {decode_token}")
            return True
        except jwt.InvalidTokenError as e:
            print(f"Invalid token: {e}")
            return False


if __name__ == '__main__':
    drone_controller = DroneController()
    drone_context = DroneContext()

    secret_key = 'my_secret_key'
    token = jwt.encode({'sub': 'drone_123'}, secret_key, algorithm='HS256')

    #SafetyCheck(TakeOff(drone_controller), token).execute()
    safety_check = SafetyCheck(secret_key)
    safety_check(TakeOff(drone_controller), token).execute()

