from practise_3_13 import *
import jwt

# SECRET_KEY = 'my_token'
# https://habr.com/ru/articles/781866/



class SafetyCheck:
    def __init__(self, secret_key: str):
        self.__secret_key = secret_key

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            token = kwargs.get('token')
            if self.check_token(token):
                return func(*args, **kwargs)
            else:
                print("Token invalid")
                return None
        return wrapper


    # def execute(self):
    #     # Check
    #     if self.check_token():
    #         self.__command.execute()
    #     else:
    #         print("Safety check failed")

    def check_token(self, token):
        print("Safety check...")
        # logic
        try:
            decode_token = jwt.decode(token, self.__secret_key, algorithms=['HS256'])
            print(f"Decoded token: {decode_token}")
            return True
        except jwt.InvalidTokenError as e:
            print(f"Invalid token: {e}")
            return False

@SafetyCheck(secret_key='my_secret_key')
def drone_commands_execute(*commands, token):
    for command in commands:
        command.execute()


if __name__ == '__main__':
    drone_controller = DroneController()
    drone_context = DroneContext()

    secret_key = 'my_secret_key'
    token = jwt.encode({"sub": "drone_123"}, secret_key, algorithm='HS256')

    #SafetyCheck(TakeOff(drone_controller), token).execute()
    # safety_check = SafetyCheck(secret_key)
    # safety_check(TakeOff(drone_controller), token).execute()
    drone_commands_execute(TakeOff(drone_controller),
                         MoveForward(drone_controller, 100),
                         Turn(drone_controller, 90),
                         token=token)


