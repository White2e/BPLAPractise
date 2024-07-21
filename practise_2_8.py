#  паттерн Легковес

class DroneFlyweight:
    def __init__(self, model, manufacturer, sensors):
        self._model = model
        self._manufacturer = manufacturer
        self._sensors = sensors

    def operation(self, unique_state):
        print(f"""
        Дрон: модель {self._model}, производитель {self._manufacturer}
        Датчики: {self._sensors}
        Координаты: {unique_state["coordinates"]}
        Скорость: {unique_state["speed"]}
        Высота: {unique_state["altitude"]}
        Миссия: {unique_state["mission"]}
        Батарея: {unique_state["battery"]}        
        """)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

    @property
    def sensors(self):
        return self._sensors

    @sensors.setter
    def sensors(self, value):
        self._sensors = value


class DroneFactory:
    def __init__(self):
        self._drones = {}

    def get_drone(self, model, manufacturer, sensors):
        key = (model, manufacturer, sensors)
        if key not in self._drones:
            self._drones[key] = DroneFlyweight(model, manufacturer, sensors)
        return self._drones[key]

    def list_drones(self):
        print(f"Всего легковесных дронов {len(self._drones)}")
        for value in self._drones.keys():
            model, manufacturer, sensors = value
            print(f"""
            Ключ: Модель: {model},  Производитель: {manufacturer}, датчики {sensors}
            """)


# Клиентский код, который использует паттерн Легковес
def client_code():
    factory = DroneFactory()
    drone1 = factory.get_drone("Model 1", "Manufacturer 1", "Camera 1 GPS 1")
    drone1.operation({"coordinates": "123.456, 789.01", "speed": 80, "altitude": 50, "mission": "Полет", "battery": 100})
    drone2 = factory.get_drone("Model 1", "Manufacturer 1", "Camera 1 GPS 1")
    drone2 = factory.get_drone("Model 2", "Manufacturer 2", "Camera 1 GPS 1")
    drone2.operation({"coordinates": "987.654, 321.09", "speed": 120, "altitude": 100, "mission": "Безопасный полет", "battery": 80})
    drone2.operation({"coordinates": "987.654, 321.09", "speed": 120, "altitude": 100, "mission": "Безопасный полет", "battery": 80})
    factory.list_drones()


if __name__ == "__main__":
    client_code()
