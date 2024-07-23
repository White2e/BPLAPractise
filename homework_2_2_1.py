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



if __name__ == '__main__':
    #  Тестирование итератора
    drone_aggregator = DroneAggregator(5)
    drone_iterator = drone_aggregator.create_iterator()
    while drone_iterator.has_next():
        item = drone_iterator.next()
        print(f" {item} is available.")

print('-'*31)

# Тестирование паттерна Наблюдатель

