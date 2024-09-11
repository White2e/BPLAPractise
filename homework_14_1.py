import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


def load_data(images, labels):
    data = []
    for img in images:
        # Чтение изображения
        image = cv2.imread(img)
        # Изменение размера изображения
        image = cv2.resize(image, (64, 64))
        # Преобразование в одномерный массив
        data.append(image.flatten())
    return np.array(data), np.array(labels)


# загрузка изображений и меток (True = можно сажать, False = нельзя сажать)
images = ['img2.png', 'img3.png', 'img4.png', 'img5.png', 'img6.png']
labels = [True, False, False, False, True]
X, y = load_data(images, labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = svm.SVC()
model.fit(X_train, y_train)


# Получение изображения с камеры БПЛА (в реальном времени)
def get_uav_image():
    image = cv2.imread('img.jpeg')  # Здесь должно быть реальное изображение с камеры
    image = cv2.resize(image, (64, 64))
    return image.flatten()


uav_image = get_uav_image()
# классификация изображения
prediction = model.predict([uav_image])


def make_landing_decision(prediction):
    if prediction:
        print("Место пригодно для посадки.")
    else:
        print("Место непригодно для посадки.")


make_landing_decision(prediction)

# Оценка модели
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy * 100:.2f}%")
