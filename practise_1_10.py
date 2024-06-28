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
