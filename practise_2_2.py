# Single Responsibility Principle (Принцип единственной ответственности)
from abc import ABC, abstractmethod


class NavigationSystem:
    def calc_route(self, start, end):
        print(f"Calculate route from {start} to {end}")
        # logic
        pass


class CommunicationSystem:
    def send_data(self, data):
        print(f"Send data: {data}")
        # logic
        pass


# Open/Closed Principle (Принцип открытости/закрытости)
class FlightMode(ABC):
    @abstractmethod
    def execute(self):
        pass


class ManualMode(FlightMode):
    def execute(self):
        print("Manual operation mode")
        # logic
        pass


class AutoMode(FlightMode):
    def execute(self):
        print("Autopilot operation mode")
        # logic
        pass


class EmergencyMode(FlightMode):
    def execute(self):
        print("Emergency operation mode")
        # logic
        pass


class DestructionMode(FlightMode):
    def execute(self):
        print("Destruction mode")
        # logic
        pass

class Drone:
    def __init__(self, mode: FlightMode):
        self.__mode = mode

    def change_mode(self, new_mode: FlightMode):
        self.__mode = new_mode

    def fly(self):
        self.__mode.execute()


manual_mode = ManualMode()
destruction_mode = DestructionMode()
drone = Drone(manual_mode)
drone.fly()
drone.change_mode(destruction_mode)
drone.fly()
print("\n ---------------------------------\n")

# Liskov Substitution Principle (Принцип подстановки Лисков)


class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Camera(Sensor):
    def get_data(self):
        print("Receiving data from camera")
        return "Data from camera"


class Lidar(Sensor):
    def get_data(self):
        print("Receiving data from lidar")
        return "Data from Lidar"


class Battery(Sensor):
    def get_data(self):
        print("Receiving data from battery")
        return "Data from Battery"


class Drone2:
    def __init__(self, sensor: Sensor):
        self.__sensor = sensor

    def gather_data(self):
        data = self.__sensor.get_data()
        print(f"Collected data: {data}")


battery = Battery()
drone2 = Drone2(battery)
drone2.gather_data()
