import random
import time

altitude = 0  # Высота в метрах
speed = 0  # Скорость в метрах в секунду
weight = 1.5  # Вес БПЛА в килограммах
payload = 500  # Грузоподъемность в граммах

pitch = 0  # Тангаж в градусах
roll = 0  # Крен в градусах
yaw = 0  # Рысканье в градусах

battery_capacity = 100  # Емкость батареи в процентах
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

# int - целое
# float - вещественное
# str - строка
# list - список

propellers_speed = [0, 0, 0, 0]  # Скорость вращения пропеллеров в об/мин
propellers_direction = ["CCW", "CW", "CW", "CCW"]  # Направление вращения пропеллеров в об/мин
# print(propellers_speed[0]) - извлечь скорость 1 пропеллера

direction = 0  # Направление
is_flying = False  # Летит ли БПЛА
is_connected = False  # Подключен ли БПЛА
is_armed = False  # Арминг двигателя
speed_k = 1000  # 1 м\с = 1000 об\м

coordinates = (50.1231, 30.5231)  # начальные
target_coord = (30.2344, 42.5332)  # координаты цели

way_coords = []  # где был дрон

def get_info():
    info = f"""
    -------Квадрокоптер-------
    Высота: {altitude} м, Скорость: {speed} м/сек.
    Вес БПЛА: {weight} кг, Грузоподъемность: {speed} гр.
    Тангаж: {pitch}, Крен: {roll} Рысканье: {yaw}
    Скорость вращения пропеллеров: {propellers_speed}
    ({propellers_speed[0]})       ({propellers_speed[1]})
     CCW      CW
      \\        /
       \\      /
        ------
       /      \\
      /        \\
     CW       CCW
    ({propellers_speed[2]})       ({propellers_speed[3]})
    """
    print(info)


def drone_connect():
    global is_connected
    print("Подключение к БПЛА...")
    time.sleep(1)
    is_connected = True
    print("Подключение установлено")


def arm_drone():
    global is_armed, propellers_speed
    if is_connected:
        print("Армирование двигателя...")
        # Симулируем проверку безопасности
        time.sleep(3)
        print("Проверка безопасности завершена")
        is_armed = True
        start = 100
        propellers_speed = [start, start, start, start]  # Скорость вращения пропеллеров в об/мин
        way_coords.append(coordinates)
        print("Двигатель армирован. БПЛА ")
        print(f"Скорость вращения пропеллеров {start}")
        print(f"Направление движения пропеллеров {propellers_direction}")
    else:
        print("Армирование двигателя не удалось. БПЛА не подключен.")


def set_propellers_speed(speed):
    global propellers_speed
    if is_armed:
        propellers_speed = [speed, speed, speed, speed]
        print(f"Установлена скорость вращения пропеллеров: {propellers_speed}")
    else:
        print(f"Не удалось установить скорость вращения пропеллеров. Двигатель не армирован.")


def move_to_coord(target):
    global coordinates, altitude, speed, direction
    if is_armed and is_flying:
        print(f"Перемещаемся к координатам: {target} ...")
        coordinates = target
        altitude = 10
        speed = 6
        direction = 200
        time.sleep(5)
        print(f"Достигли цели")
        way_coords.append(coordinates)


get_info()
drone_connect()
arm_drone()
get_info()

if is_armed and is_connected:
    set_propellers_speed(1000)
    print("Взлет!")
    speed = 5
    altitude = 10
    pitch = 15
    roll = 5
    yaw = 10
    direction = 90
    is_flying = True
    battery_capacity -= 5
    coordinates = (50.1231, 30.5231)
    telemetry = {
        "speed": speed,
        "altitude": altitude,
        "pitch": pitch,
        "roll": roll,
        "yaw": yaw,
        "direction": direction,
        "propellers_speed": propellers_speed,
        "propellers_direction": propellers_direction,
        "coordinates": coordinates,
        "battery_capacity": battery_capacity
    }
    print(f"Телеметрия: {telemetry}")
else:
    print(f"Взлететь не удалось.")

if is_flying:
    move_to_coord(target_coord)

get_info()
print(f"Путь: {way_coords}")
way_coords[0] = (random.randint(1, 50), random.randint(1, 50))