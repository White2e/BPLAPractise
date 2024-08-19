from abc import ABC, abstractmethod
from practise_3_14_2 import *


class DroneController():
    # def __init__(self, drone):
    #     self.__drone = drone
    #     self.__commands = []

    def takeoff(self):
        print("Drone takeoff ...")

    def move_forward(self, distance: float):
        print(f"Drone move forward {distance} meters ...")

    def turn(self, degree: float):
        print(f"Drone degree {degree} grade ...")


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    # @abstractmethod
    # def undo(self):
    #     pass


class TakeOff(ICommand):
    def __init__(self, drone: DroneController):
        self.__drone = drone

    def execute(self):
        self.__drone.takeoff()


class MoveForward(ICommand):
    def __init__(self, drone: DroneController, distance: float):
        self.__drone = drone
        self.__distance = distance

    def execute(self):
        self.__drone.move_forward(self.__distance)


class Turn(ICommand):
    def __init__(self, drone: DroneController, degree: float):
        self.__drone = drone
        self.__degree = degree

    def execute(self):
        self.__drone.turn(self.__degree)

class IFlightStrategy(ABC):
    @abstractmethod
    def execute(self, commands: list):
        pass


class ReconMissionStrategy(IFlightStrategy):
    @SafetyCheck(secret_key='my_secret_key')
    def execute(self, commands: list, token: None):
        print("Start Recon mission strategy:")
        for command in commands:
            command.execute()
        print("End Recon mission strategy:")


class DroneContext:
    def __init__(self, strategy: IFlightStrategy=None):
        self.__strategy = strategy
        self.__commands = []

    def set_strategy(self, strategy: IFlightStrategy):
        self.__strategy = strategy

    def add_command(self, command: ICommand):
        self.__commands.append(command)

    def execute(self, token=None):
        self.__strategy.execute(self.__commands, token=token)
        self.__commands.clear()


class PatrolMissionStrategy(IFlightStrategy):
    def __init__(self, n_patrols: int):
        self.__n_patrols = n_patrols

    @SafetyCheck(secret_key='my_secret_key')
    def execute(self, commands: list, token: None):
        print(f"Start mission...")
        for _ in range(self.__n_patrols):
            for command in commands:
                command.execute()
            print("End patrol")
        print("End mission")


if __name__ == '__main__':

    secret_key = 'my_secret_key'
    token = jwt.encode({"sub": "drone_123"}, secret_key, algorithm='HS256')

    drone_controller = DroneController()
    takeoff = TakeOff(drone_controller)
    move_forward = MoveForward(drone_controller, 100)
    takeoff.execute()
    move_forward.execute()

    commands = [
        TakeOff(drone_controller),
        MoveForward(drone_controller, 100),
        MoveForward(drone_controller, -100)
    ]

    strategy = ReconMissionStrategy()
    strategy.execute(commands)

    context = DroneContext()
    context.set_strategy(ReconMissionStrategy())

    context.add_command(TakeOff(drone_controller))
    context.add_command(MoveForward(drone_controller, 100))
    context.add_command(MoveForward(drone_controller, -100))
    context.execute(token=token)

    context.set_strategy(PatrolMissionStrategy(n_patrols=3))
    for _ in range(4):
        context.add_command(MoveForward(drone_controller, 100))
        context.add_command(Turn(drone_controller, 90))
    context.execute(token=token)
