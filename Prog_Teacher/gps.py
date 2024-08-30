import airsim
import time

# Подключение к симулятору
client = airsim.MultirotorClient()
client.confirmConnection()

# Разблокировка управления и взлет
client.enableApiControl(True)
client.armDisarm(True)

# Взлет до высоты 3 метра
client.takeoffAsync().join()
client.moveToZAsync(-3, 1).join()

# Полет вперед на 10 метров со скоростью 5 м/с
client.moveToPositionAsync(10, 0, -3, 5).join()

# Получение данных с GPS
gps_data = client.getGpsData()

# Вывод данных GPS
print(f"Широта: {gps_data.gnss.geo_point.latitude} °")
print(f"Долгота: {gps_data.gnss.geo_point.longitude} °")
print(f"Высота: {gps_data.gnss.geo_point.altitude} м")

# Приземление
client.landAsync().join()

# Отключение управления
client.armDisarm(False)
client.enableApiControl(False)

print("Полёт завершен успешно!")
