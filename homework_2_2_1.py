from abc import ABC, abstractmethod
from typing import List


#  Реализация паттерна Итератор
#  В данном примере создается итератор для опроса дронов в рое дров

class Drone:
    def __init__(self, drone_list):
        self.drone_list = drone_list
        self.index = 0

    def __str__(self):
        return f'Current drone: {self.drone_list}'


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Drone:
        pass


class DroneIterator(Iterator):
    def __init__(self, drone: List[Drone]):
        self._drone = drone
        self._index = 0

    def next(self) -> Drone:
        if self.has_next():
            drone = self._drone[self._index]
            self._index += 1
            return drone
        else:
            raise StopIteration

    def has_next(self) -> bool:
        return self._index < len(self._drone)


class DroneAggregator:
    def __init__(self, drone_count: int):
        self.count = [Drone(i+1) for i in range(drone_count)]

    def amount_of_drones(self) -> int:
        return len(self.count)

    def create_iterator(self) -> Iterator:
        return DroneIterator(self.count)


#  Реализация паттерна Наблюдатель
class MyObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class MySubject:
    def __init__(self):
        self._observers = []

    def register(self, observer: MyObserver):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


class AlertSystem(MyObserver):
    def update(self, message: str):
        print(f"Система предупреждения получила сообщение {message}")


class AnalyseSystem(MyObserver):
    def update(self, message: str):
        print(f"Система анализа получила сообщение {message}")


class DroneObservable(MySubject):
    def __init__(self):
        super().__init__()
        self._altitude = 0

    def set_altitude(self, altitude: int):
        self._altitude = altitude
        self.notify(f"Высота дрона изменена на {altitude} метров")
        if self._altitude > 500:
            self.notify(f"Высота дрона превысила допустимую {self._altitude}м, ВНИМАНИЕ!")


#  Реализация паттерна Шаблонный метод
class MyBase(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass


class MyClass1(MyBase):
    def step1(self):
        print("MyClass1: Реализация шага 1")

    def step2(self):
        print("MyClass1: Реализация шага 2")

    def step3(self):
        print("MyClass1: Реализация шага 3")


class MyClass2(MyBase):
    def step1(self):
        print("MyClass2: Реализация шага 1")

    def step2(self):
        print("MyClass2: Реализация шага 2")

    def step3(self):
        print("MyClass2: Реализация шага 3")



if __name__ == '__main__':
    #  Тестирование итератора
    print("Тестирование паттерна Итератор:")
    print("Собираем рой дронов, где количество дронов - 5:")
    drone_aggregator = DroneAggregator(5)
    print("Опрос дронов:")
    drone_iterator = drone_aggregator.create_iterator()
    while drone_iterator.has_next():
        item = drone_iterator.next()
        print(f" {item} is available.")

print('-'*31)

# Тестирование паттерна Наблюдатель
print("Тестирование паттерна Наблюдатель:")
alert_system = AlertSystem()
analyse_system = AnalyseSystem()
drone_observable = DroneObservable()
drone_observable.register(alert_system)
drone_observable.register(analyse_system)
drone_observable.set_altitude(100)
drone_observable.set_altitude(600)

print('-'*31)

# Тестирование паттерна Шаблонный метод
print("Тестирование шаблонного метода:")
my_class1 = MyClass1()
my_class1.template_method()
print()
my_class2 = MyClass2()
my_class2.template_method()

print('-'*31)
