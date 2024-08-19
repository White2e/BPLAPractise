from practise_3_13 import *


class SafetyCheck(ICommand):
    def __init__(self, command: ICommand, token: str):
        self.__command = command
        self.__token = token

    def execute(self):
        # Check
        if self.check_token():
            self.__command.execute()
        else:
            print("Safety check failed")

    def check_token(self):
        print("Safety check...")
        # logic
        if self.__token == "my_token":
            print("Token valid")
            return True
        else:
            print("Token invalid")
            return False


if __name__ == '__main__':
    drone_controller = DroneController()
    drone_context = DroneContext()

    token = 'my_token'

    SafetyCheck(TakeOff(drone_controller), token).execute()

