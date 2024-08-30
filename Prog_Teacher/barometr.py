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

# Получение данных с барометра
barometer_data = client.getBarometerData()

# Вывод данных барометра
print(f"Давление: {barometer_data.pressure} Па")
print(f"Высота над уровнем моря: {barometer_data.altitude} м")

# Приземление
client.landAsync().join()

# Отключение управления
client.armDisarm(False)
client.enableApiControl(False)

print("Полёт завершен успешно!")
