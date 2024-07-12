# паттерн мост
from abc import ABC, abstractmethod


class Drone(ABC):
    def __init__(self, engine):
        self.engine = engine

    @abstractmethod
    def fly(self):
        pass


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def set_rotation_speed(self, speed: int):
        pass

class SingleEngine(Engine):
    def start(self):
        return "Запуск двигателей"

    def stop(self):
        return "Остановка двигателей"

    def status(self):
        return "Статус одного двигателя"

    def set_rotation_speed(self, speed: int):
        power = speed * 10 # каждый процент скорости потребляет 10 ма
        # return f"скорость вращения одного двигателя установлена на {speed} двигателей"
        print(f"скорость вращения одного двигателя установлена на {speed}%")
        return power



class TripleEngine(Engine):
    def start(self):
        return "Запуск двигателей"

    def stop(self):
        return "Остановка двигателей"

    def status(self):
        return "Статус трех двигателей"

    def set_rotation_speed(self, speed: int):
        power = speed * 30  # каждый процент скорости потребляет 10 ма
        # return f"скорость вращения одного двигателя установлена на {speed} двигателей"
        print(f"скорость вращения трех двигателей установлена на {speed}%")
        return power


class QuadEngine(Engine):
    def start(self):
        return "Запуск двигателей"

    def stop(self):
        return "Остановка двигателей"

    def status(self):
        return "Статус четырех двигателей"

    def set_rotation_speed(self, speed: int):
        power = speed * 40  # каждый процент скорости потребляет 10 ма
        # return f"скорость вращения одного двигателя установлена на {speed} двигателей"
        print(f"скорость вращения четырех двигателей установлена на {speed}%")
        return power


class StandartDrone(Drone):
    def fly(self):
        print(self.engine.start())
        print("Стандартный дрон в полете")
        speed = 50  # двигатель запущен на 50% мощности
        print(f" потребляемый ток self.engine.set_rotation_speed(50)")
        print(self.engine.status())
        print(self.engine.stop())


class AdvancedDrone(Drone):
    def fly(self):
        print(self.engine.start())
        print("Стандартный дрон в полете")
        speed = 50  # двигатель запущен на 50% мощности
        print(f" потребляемый ток self.engine.set_rotation_speed(50)")
        print(self.engine.status())
        print(self.engine.stop())

    def get_status(self):
        print(self.engine.status())

    def set_speed(self, speed: int):
        current = self.engine.set_rotation_speed(speed)
        print(f"установлена скорость {speed}, ток {self.engine.set_rotation_speed(speed)}")


if __name__ == '__main__':
    single_engine = SingleEngine()
    triple_engine = TripleEngine()
    quad_engine = QuadEngine()

    standart_drone = StandartDrone(single_engine)
    advanced_drone = AdvancedDrone(quad_engine)

    standart_drone.fly()
    print()
    advanced_drone.fly()
    advanced_drone.set_speed(75)
    advanced_drone.get_status()
    print()
    print("Замена двигателя")
    advanced_drone.engine = triple_engine
    advanced_drone.fly()
    advanced_drone.get_status()
