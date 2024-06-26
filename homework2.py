import random


class Drone:
    def __init__(self, id="HW02",
                 max_altitude=300,
                 max_speed=60):
        self.__id = id
        self.__max_altitude = max_altitude
        self.__max_speed = max_speed
        self.__cur_altitude = 0
        self.__cur_speed = 0
        self.__cur_coord = (0.0, 0, 0)
        self.__coord = (0.0, 0, 0)
        self.__flight_path = []

    def set_max_altitude(self, max_altitude: float):
        if max_altitude > 0 and max_altitude < 3000:
            self.__max_altitude = max_altitude
        else:
            raise ValueError("Неверное значение максимальной высоты")

    def get_max_altitude(self):
        return self.__max_altitude

    def set_max_speed(self, max_speed: float):
        if max_speed > 0:
            self.__max_speed = max_speed
        else:
            raise ValueError("Неверное значение максимальной скорости")

    def get_max_speed(self):
        return self.__max_speed

    def set_cur_altitude(self, cur_altitude: float):
        self.__cur_altitude = cur_altitude

    def get_cur_altitude(self):
        return self.__cur_altitude


class GPS:
    def __init__(self, init_coordinates=(0.0, 0.0)):
        self.coordinates = init_coordinates

    def update_coordinates(self):
        lat_variation = random.uniform(-0.0001, 0.0001)  # широта
        lon_variation = random.uniform(-0.0001, 0.0001)  # долгота
        lat = round(self.coordinates[0] + lat_variation, 4)
        lon = round(self.coordinates[1] + lon_variation, 4)
        self.coordinates = (lat, lon)
        print(f"Текущие координаты: {self.coordinates}")
        return self.coordinates


class FlightController:
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
