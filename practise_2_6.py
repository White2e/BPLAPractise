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
        print(f"Система логирования получила сообщение: {message}")
        if image is not None:
            self.save_image(image)

    @staticmethod
    def save_image(image):
        filename = "camera.png"
        cv2.imwrite(filename, image)
        print(f"Снимок сделан {filename}")


class AlertSystem(Observer):
    def update(self, message: str, image=None):
        print(f"Система предупреждения получила сообщение {message}")


class AnalyseSystem(Observer):
    def update(self, message: str, image=None):
        print(f"Система анализа получила сообщение {message}")


class Camera(Observable):
    def __init__(self):
        super().__init__()
        self._zoom_lvl = 1.0

    def set_zoom(self, zoom_lvl: float):
        self._zoom_lvl = zoom_lvl
        self.notify_observers(f"Изменен зум на {self._zoom_lvl}")

    def take_image(self):
        caption = cv2.VideoCapture(0)
        ret, frame = caption.read()
        if ret:
            self.notify_observers("Захвачено изображение", frame)
        caption.release()


data_logger = DataLogger()
alert_system = AlertSystem()
analyse_system = AnalyseSystem()

camera = Camera()

camera.add_observer(data_logger)
camera.add_observer(alert_system)
camera.add_observer(analyse_system)

camera.set_zoom(2.0)
camera.take_image()
