class Drone:
    def __init__(self, id="ABC123",
                 max_altitude=300,
                 max_speed=60,
                 flight_time=30,
                 weight=1.5):
        self.__id = id
        self.__max_altitude = max_altitude
        self.__max_speed = max_speed
        self.__flight_time = flight_time
        self.__weight = weight
        self.__cur_altitude = 0
        self.__cur_speed = 0
        self.__cur_coord = (0.0, 0,0)
        self.__coord = (0.0, 0,0)
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

    def set_flight_time(self, flight_time: float):
        if flight_time > 0:
            self.__flight_time = flight_time
        else:
            raise ValueError("Неверное значение времени полета")

    def get_flight_time(self):
        return self.__flight_time

    def set_cur_altitude(self, altitude):
        if 0 <= altitude <= self.__max_altitude:
            self.__cur_altitude = altitude
        else:
            raise ValueError(f"Высота должна быть в диапазоне от 0 до {self.__max_altitude}")

    def get_cur_altitude(self):
        return self.__cur_altitude

    def get_flight_path(self):
        return self.__flight_path

    def add_waypoint(self, coord: tuple):
        self.__flight_path.append(coord)
        print(f"Добавлена новая точка маршрута: {self.__flight_path[-1]}")

    def set_cur_coord(self, coord: tuple):
        self.__cur_coord = coord

    def get_cur_coord(self):
        return self.__cur_coord

    def follow_flight_path(self):
        #if self.__flight_path != []:
        if not self.__flight_path:
            print(f"Маршрут не задан")
            return
        #else:
        print(f"{self.__id} следует по маршруту")
        for waypoint in self.__flight_path:
            # добавить установку координат
            self.set_cur_coord(waypoint)
            print(f"Достигнута точка {self.__cur_coord}")


class ProfessionalDrone(Drone):
    def __init__(self, id="CDF1258",
                max_altitude = 300,
                max_speed = 60,
                flight_time = 30,
                weight = 1.5):
        super().__init__(id, max_altitude, max_speed, flight_time, weight)
        self.__night_vision = True




if __name__ == "__main__":
    drone1 = Drone(id="D0001", flight_time=35)
    #print(drone1.__dict__)
    drone1.set_max_altitude(350)
    print(drone1.get_max_altitude())
    drone1.set_cur_coord((55.7555, 37.2589))
    drone1.add_waypoint((48.8558, 5.5892))
    drone1.add_waypoint((67.8588, 15.5822))
    drone1.add_waypoint((18.8558, 25.1892))
    drone1.follow_flight_path()