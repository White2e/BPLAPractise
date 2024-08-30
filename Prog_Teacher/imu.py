import airsim
import time

"""
IMU (Inertial Measurement Unit, инерциальный измерительный блок)
это электронное устройство, которое измеряет и отслеживает угловую скорость, ускорение и 
иногда магнитное поле для определения положения объекта в пространстве. 

IMU обычно состоит из трех основных компонентов:
    Акселерометр: Измеряет линейное ускорение по трём осям (X, Y, Z). 
                  Это помогает определить изменения скорости и наклона объекта.

    Гироскоп: Измеряет угловую скорость вокруг трёх осей. 
              Это устройство помогает отслеживать, как быстро объект вращается в пространстве и в каком направлении.
    
    Магнитометр (не всегда включен в IMU): Измеряет магнитное поле Земли и используется для определения ориентации
                                           по отношению к северу. Это похоже на работу компаса.
"""

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

# Получение данных с IMU
imu_data = client.getImuData()

# Вывод данных IMU
print(f"Ускорение по оси X: {imu_data.linear_acceleration.x_val} м/с²")
print(f"Ускорение по оси Y: {imu_data.linear_acceleration.y_val} м/с²")
print(f"Ускорение по оси Z: {imu_data.linear_acceleration.z_val} м/с²")
print(f"Угловая скорость по оси X: {imu_data.angular_velocity.x_val} рад/с")
print(f"Угловая скорость по оси Y: {imu_data.angular_velocity.y_val} рад/с")
print(f"Угловая скорость по оси Z: {imu_data.angular_velocity.z_val} рад/с")

# Получение углов ориентации (Тангаж, Крен, Рысканье)
orientation = imu_data.orientation
pitch, roll, yaw = airsim.to_eularian_angles(orientation)

print(f"Тангаж (Pitch): {pitch} рад")
print(f"Крен (Roll): {roll} рад")
print(f"Рысканье (Yaw): {yaw} рад")

# Приземление
client.landAsync().join()

# Отключение управления
client.armDisarm(False)
client.enableApiControl(False)

print("Полёт завершен успешно!")
