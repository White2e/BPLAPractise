import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ID БПЛА | Время полета (минуты) | Расстояние (километры) | Средняя скорость (км/ч) | Высота полета (метры)

drones_data = np.array([[1, 30, 10, 20, 500], [2, 45, 15, 20, 600], [3, 25, 8, 19.2, 550], [4, 60, 25, 25, 700], [5, 35, 12, 20.6, 580]])
print(f"Данные о полетах")
print(drones_data)

altitudes = drones_data[:, 4]
max_altitudes = np.max(altitudes)
print(f"Максимальная высота полета: {max_altitudes}")

long_flight_drones = drones_data[drones_data[:, 1] > 30]  # фильтруем строки массива на основании бинарного вектора, сформированного по условию
print(long_flight_drones)

total_dist = np.sum(drones_data[:, 2])
print(f"Всего пройдено: {total_dist}")

drone_idds = drones_data[:, 0]
flight_times = drones_data[:, 1]
altitudes = drones_data[:, 4]

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.bar(drone_idds, flight_times, color='blue')
plt.xlabel('ID БПЛА')
plt.ylabel('Время полета (минуты)')
plt.title('Время полета БПЛА')

plt.subplot(1, 2, 2)
plt.bar(drone_idds, altitudes, color='red')
plt.xlabel('ID БПЛА')
plt.ylabel('Высота полета (минуты)')
plt.title('Высота полета БПЛА')

plt.show()

convertation_matrix = np.array([
    [1, 0],
    [0, 0.277778]
])

speed_kmh = drones_data[:, 3]
speed_ms = speed_kmh * convertation_matrix[1, 1]

print(f"Скорость - {speed_kmh} км/ч")
print(f"Скорость - {speed_ms} м/с")
