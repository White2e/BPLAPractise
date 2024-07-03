import pandas as pd
import matplotlib.pyplot as plt

# создаем два списка
# месяцы
list1 = []
for i in range(1, 13):
    list1.append(i)
# температура
list2 = [-15, -25, -10, 0, 15, 25, 35, 37, 28, 18, 5, -10]

# рисуем график
plt.figure(figsize=(10, 5))
plt.plot(list1, list2, marker=".")
plt.xlabel("Месяц")
plt.ylabel("Температура")
plt.title("Температура по месяцам")
plt.legend("С")
plt.grid(True, "both")
plt.show()

