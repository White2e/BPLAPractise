class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"Сделано фото с разрешением {self.resolution}")

class GPS:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0

    def update_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        print(f"Обновление координат - Latitude: {self.latitude}, Longitude: {self.longitude}")

class FlightController:
    def __init__(self):
        self.altitude = 0.0
        self.latitude = 0.0
        self.longitude = 0.0

    def takeoff(self):
        self.altitude = 10.0
        print(f"Дрон взлетает - высота {self.altitude} метров")

    def land(self):
        self.altitude = 0.0
        print("Дрон приземлился")

    def change_altitude(self, altitude):
        self.altitude = altitude
        print(f"Изменение высоты на {self.altitude} метров")

    def change_coordinates(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        print(f"Изменение координат - Latitude: {self.latitude}, Longitude: {self.longitude}")

class Drone:
    def __init__(self, camera, gps, flight_controller):
        self.camera = camera
        self.gps = gps
        self.flight_controller = flight_controller


if __name__ == "__main__":

    # Создаем объекты компонентов
    camera = Camera("1080p")
    gps = GPS()
    flight_controller = FlightController()

    # Создаем объект беспилотника с компонентами
    drone = Drone(camera, gps, flight_controller)

    # Управление полетом беспилотника
    drone.flight_controller.takeoff()
    drone.flight_controller.change_altitude(20)
    drone.flight_controller.change_coordinates(51.7558, 47.6176)
    drone.flight_controller.land()

    # Работа с камерой и GPS
    drone.camera.take_photo()
    drone.gps.update_location(51.7558, 47.6176)
