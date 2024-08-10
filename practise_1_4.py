from practise_1_5 import GPS, DistanceSensor

class Drone:
  brand = "БПЛА РФ"
  n_rotors = 4

  def __init__(self, model, weight, payload, id):
    print(f"Создание экземпляра  {self.__class__.__name__}")
    self.id = id
    self.weight = weight
    self.payload = payload
    self.model = model
    self.altitude = 0  # Высота в метрах
    self.speed = 0  # Скорость в метрах в секунду
    self.weight = weight  # Вес БПЛА в килограммах
    self.payload = payload  # Грузоподъемность в граммах
    self.pitch = 0  # Тангаж в градусах (Поворот вокруг поперечной оси (наклон вперед или назад))
    self.roll = 0  # Крен в градусах (Поворот вокруг продольной оси (наклон влево или вправо))
    self.yaw = 0  # Рысканье в градусах (Поворот вокруг вертикальной оси)
    self.battery_capacity = 100  # Емкость батареи в процентах
    # Против часовой стрелки (CCW)
    # По часовой стрелке (CW)
    # (1)       (2)
    #  CCW      CW
    #   \        /
    #    \      /
    #     ------
    #    /      \
    #   /        \
    #  CW       CCW
    # (3)       (4)

    # int - целое число
    # float - вещественное число
    # str - строка
    # list - список
    # tuple - кортеж
    self.propellers_speed = [0, 0, 0, 0]  # Скорость вращения пропеллеров в об/мин
    self.propellers_direction = ["CCW", "CW", "CW", "CCW"]  # Направление вращения пропеллеров
    # print(propellers_speed[0]) - извлечь скорость 1 пропеллера
    self.direction = 0  # Направление
    self.is_flying = False  # Летит ли БПЛА
    self.is_connected = False  # Подключен ли БПЛА
    self.is_armed = False  # Арминг двигателя
    self.speed_k = 1000  # 1 м/с = 1000 об/мин
    self.coordinates = (50.1231, 30.5231)  # начальные координаты
    self.cur_coordinates = (50.1231, 30.5231)  # текущие координаты
    self.target_coord = (30.2344, 42.5332)  # координаты цели
    self.way_coords = []  # где был дрон, его координаты
    self.gps = GPS(self.coordinates)  # создание экземпляра класса GPS
    self.dist_sensor = DistanceSensor()

  def get_dist(self):
    return self.dist_sensor.get_dist()
  
  def get_coords(self):
    self.cur_coordinates = self.gps.update_coordinates()
    print(f"id: {self.id} Координаты: {self.cur_coordinates}")

  def __del__(self):
    print(f"Удаление экземпляра  {self.__class__.__name__}")
    
  def fly(self):
    pass

  def get_info(self):
    print(f"Модель: {self.model}, Вес: {self.weight}, Грузоподъемность: {self.payload}")
    info = f"""
    -------Квадрокоптер-------
    Бренд: {self.brand} Модель: {self.model}
    Количество роторов: {self.n_rotors}
    Высота: {self.altitude} м, Скорость: {self.speed} м/сек.
    Вес БПЛА: {self.weight} кг, Грузоподъемность: {self.payload} кг.
    Тангаж: {self.pitch}, Крен: {self.roll} Рысканье: {self.yaw}
    Скорость вращения пропеллеров: {self.propellers_speed}
    ({self.propellers_speed[0]})       ({self.propellers_speed[1]})
     CCW      CW
      \\        /
       \\      /
        ------
       /      \\
      /        \\
     CW       CCW
    ({self.propellers_speed[2]})       ({self.propellers_speed[3]})
    """
    print(info)


if __name__ == "__main__":
  drone1 = Drone("Model1", 3, 2, "T-1000")
  drone2 = Drone("Model2", 3, 2, "T-1001")
  drone1.get_coords()
  drone1.cur_coordinates = (50.1231, 31.5231)
  drone1.get_coords()
  drone2.get_coords()

  drone1.get_info()
  drone2.get_info()