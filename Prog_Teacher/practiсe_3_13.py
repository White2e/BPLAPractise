from abc import ABC, abstractmethod


class DroneController:
    def takeoff(self):
        print('Дрон взлетает...')

    def move_forward(self, distance: float):
        print(f"Летим вперед на {distance} метров")

    def turn(self, degree: float):
        print(f"Поворачиваем на {degree} градусов")

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    # def undo(self):
    #     pass


class Takeoff(ICommand):
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

# Стратегия разведывательной миссии
class ReconMissionStrategy(IFlightStrategy):
    def execute(self, commands: list):
        print(f"Начало выполнения разведывательной миссии")
        for command in commands:
            command.execute()
        print(f"Конец миссии")

class PatrolMissionStrategy(IFlightStrategy):
    def __init__(self, n_patrols: int):
        self.__n_patrols = n_patrols

    def execute(self, commands: list):
        print(f"Начало выполнения миссии патрулирования")
        for _ in range(self.__n_patrols):
            for command in commands:
                command.execute()
            print("Патрулирование выполнено")
        print(f"Конец миссии")

class DroneContext:
    def __init__(self, strategy: IFlightStrategy=None):
        self.__strategy = strategy
        self.__commands = []

    def set_strategy(self, strategy: IFlightStrategy):
        self.__strategy = strategy

    def add_command(self, command: ICommand):
        self.__commands.append(command)

    def execute(self):
        self.__strategy.execute(self.__commands)
        self.__commands.clear()


