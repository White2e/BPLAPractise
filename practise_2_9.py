#  паттерн Легковес

import time, math, matplotlib.pyplot as plt


class CoordinateFlyweight:
    _coordinates = {}
    # def __init__(self, latitude, longitude):
    #     self._latitude = latitude
    #     self._longitude = longitude

    @staticmethod
    def get_coordinates(latitude, longitude):
        key = (latitude, longitude)
        if key not in CoordinateFlyweight._coordinates:
            CoordinateFlyweight._coordinates[key] = key
        return CoordinateFlyweight._coordinates[key]


# паттерн Proxy

class DJIDroneProxy:
    def __init__(self, real_drone):
        self._real_drone = real_drone

    def global_position_control(self, latitude=None, longitude=None, altitude=None):
        print(f"Запрос глобальных координат...  {latitude}, {longitude}, {altitude}")
        # обращаемся к SDK дрона для получения координат
        self._real_drone.global_position_control(latitude, longitude, altitude)
        # time.sleep(1)  # для ускорения отключаем -  ожидаем получение координат
        print("Глобальные координаты получены")

    def connect(self):
        print("Подключаемся к дрону...")
        self._real_drone.request_sdk_permission_control()
        time.sleep(1)  # ожидаем подключения

    def takeoff(self):
        print("Взлетаем...")
        self._real_drone.takeoff()
        time.sleep(5)  # ожидаем взлета

    def land(self):
        print("Приземляемся...")
        self._real_drone.land()
        time.sleep(3)  # ожидаем приземления

    def arm(self):
        print("Армирование дрона...")
        self._real_drone.arm()
        time.sleep(1)  # ожидаем армирования


class DJIDrone:
    def global_position_control(self, latitude=None, longitude=None, altitude=None):
        print(f"Изменяем глобальные координаты на {latitude}, {longitude}, {altitude}")

    def request_sdk_permission_control(self):
        print("Запрашиваем разрешение на использование SDK")

    def takeoff(self):
        print("Взлетаем")

    def land(self):
        print("Приземляемся")

    def arm(self):
        print("Приводим дрон в автоматический режим")


min_latitude, max_latitude = 57.826873, 57.922174
min_longitude, max_longitude = 55.475823, 55.671439

begin_latitude = min_latitude + (max_latitude - min_latitude) / 2
begin_longitude = min_longitude + (max_longitude - min_longitude) / 2

step = 0.00005
altitude = 50

real_drone = DJIDrone()
drone = DJIDroneProxy(real_drone)

coordinates = []


def spiral(drone):
    radius = 0
    angle = 0
    while radius <= (max_longitude - min_longitude)/2:
        radius += step
        angle += math.pi / 180
        x = math.sin(angle) * radius
        y = math.cos(angle) * radius
        lat_current = begin_latitude + x
        lon_current = begin_longitude + y
        coordinates.append(CoordinateFlyweight.get_coordinates(lat_current, lon_current))
        # drone.global_position_control(latitude=lat_current, longitude=lon_current, altitude=random.randint(0, 300))
        drone.global_position_control(latitude=lat_current, longitude=lon_current, altitude=altitude)
        # time.sleep(1)


drone.connect()
time.sleep(1)
drone.arm()
time.sleep(1)
drone.takeoff()
time.sleep(1)

spiral(drone)

drone.global_position_control(latitude=begin_latitude, longitude=begin_longitude, altitude=altitude)
time.sleep(1)
drone.land()

# визуализация координат
print(*coordinates, sep='\n' )
latitudes, longitudes = zip(*coordinates)
plt.plot(longitudes, latitudes)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# drone.disarm()
