import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


df = pd.read_csv('drone_flight_data.csv')
df["Скорость разряда (мАч/с)"] = df["Уровень заряда (мАч)"].diff() / df["Время (с)"].diff()
df = df.dropna()

print(df.head())
plt.figure(figsize=(10, 8))


plt.plot(df["Время (с)"], df["Высота (м)"], label="Высота", color='blue')
plt.plot(df["Время (с)"], df["Скорость (км/ч)"], label="Скорость", color='red')
plt.plot(df["Время (с)"], df["Температура"], label="Скорость", color='red')

plt.title("Зависимость высоты и скорости от времени")
plt.legend()
plt.show()