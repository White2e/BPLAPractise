import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


df = pd.read_csv('dataset.csv')
###
data = {
    'Время (с)': [0, 10, 20, 30, 40, 50, 60],
    'Уровень заряда (мАч)': [1000, 980, 960, 940, 920, 900, 880],
    'Температура': [15, 15, 15, 15, 15, 15, 15]
}
df = pd.DataFrame(data)
###
df["Скорость разряда (мАч/с)"] = df["Уровень заряда (мАч)"].diff() / df["Время (с)"].diff()
df = df.dropna()

print(df["Температура"])
# plt.figure(figsize=(10, 8))
#
#
# plt.plot(df["Время (с)"], df["Высота (м)"], label="Высота", color='blue')
# plt.plot(df["Время (с)"], df["Скорость (км/ч)"], label="Скорость", color='red')
# plt.plot(df["Время (с)"], df["Температура"], label="Скорость", color='red')
#
# plt.title("Зависимость высоты и скорости от времени")
# plt.legend()
# plt.show()


X = df[["Температура", "Время (с)"]]
y = df["Скорость разряда (мАч/с)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

mlp = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=1000, random_state=42)

mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print(f"Среднеквадратичная ошибка: {mse}")

new_data = pd.DataFrame([[70, 800]], columns=["Время (с)", "Уровень заряда (мАч)"])

new_data = StandardScaler().fit_transform(new_data)

prediction = mlp.predict(new_data)
print(f"Время до разрядки: {800/-prediction} с")