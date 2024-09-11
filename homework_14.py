import numpy as np
import cv2  # Для работы с изображениями
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Шаг 1: Загрузка и предобработка данных
def load_data(images, labels):
    data = []
    for img in images:
        image = cv2.imread(img)  # Чтение изображения
        image = cv2.resize(image, (64, 64))  # Изменение размера изображения
        data.append(image.flatten())  # Преобразование в одномерный массив
    return np.array(data), np.array(labels)

# Пример загрузки изображений и меток (True = можно сажать, False = нельзя сажать)
images = ['image1.jpg', 'image2.jpg', 'image3.jpg']  # Пример пути к изображениям
labels = [True, False, True]  # Пример меток
X, y = load_data(images, labels)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Шаг 2: Обучение модели (выбираем SVM или дерево решений)
model = svm.SVC()  # Или используйте DecisionTreeClassifier()
# model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Шаг 3: Получение изображения с камеры БПЛА (в реальном времени)
def get_uav_image():
    # Пример получения изображения с камеры
    image = cv2.imread('uav_image.jpg')  # Здесь должно быть реальное изображение с камеры
    image = cv2.resize(image, (64, 64))
    return image.flatten()

uav_image = get_uav_image()

# Применение модели для классификации изображения
prediction = model.predict([uav_image])

# Шаг 4: Принятие решения о посадке
def make_landing_decision(prediction):
    if prediction:
        print("Место пригодно для посадки.")
    else:
        print("Место непригодно для посадки.")

make_landing_decision(prediction)

# Оценка модели на тестовых данных
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy * 100:.2f}%")
