import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

df = pd.read_csv('drone_flight_data1.csv')

# переопределение датасета --------------------
data = {
    'Время (с)': [0, 10, 20, 30, 40, 50, 60],
    'Уровень заряда (мАч)': [1000, 980, 960, 940, 920, 900, 880],
    'Температура': [15, 15, 15, 15, 15, 15, 15],
    'Высота (м)': [105, 95, 100, 90, 91, 92, 95]
}
df = pd.DataFrame(data)
# ---------------------------------------------

df["Скорость разряда (мАч/)"] = df["Уровень заряда (мАч)"] / df["Время (с)"].diff()
df = df.dropna()

print(df.head())
plt.figure(figsize=(10, 8))

plt.plot(df["Время (с)"], df["Высота (м)"], label="Высота")
plt.plot(df["Время (с)"], df["Скорость (км/ч)"], label="Скорость")
plt.plot(df["Время (с)"], df["Температура"], label="Температура")

plt.title("Зависимость высоты и скорости от времени")
plt.legend()
plt.show()

X = df[["Температура", "Время (с)"]]
y = df["Скорость разряда (мАч/)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

mlp = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=1000, random_state=42)
mlp.fit(X_train, y_train)

predictions = mlp.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print("Mean Squared Error:", mse)

new_data = pd.DataFrame([[70, 800]], columns=["Время (с)", "Уровень заряда (мАч)"])
new_data = StandardScaler().fit_transform(new_data)
predicted_speed = mlp.predict(new_data)

print("Предсказанная скорость разряда:", 800/-predicted_speed)