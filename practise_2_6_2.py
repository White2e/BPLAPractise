# паттерн Наблюдатель
from abc import ABC, abstractmethod
import cv2


class Observer(ABC):
    @abstractmethod
    def update(self, message: str, image=None):
        pass


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, message: str, image=None):
        for observer in self._observers:
            observer.update(message, image)


class DataLogger(Observer):
    def update(self, message: str, image=None):
        print(f"Система записи получила сообщение {message}")
        if image is not None:
            self.save_image(image)
            
