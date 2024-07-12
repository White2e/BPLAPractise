# паттерн Наблюдатель
from abc import ABC, abstractmethod


class Observer:
    def update(self, message: str):
        pass


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)



    