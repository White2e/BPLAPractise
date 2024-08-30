import airsim
import time
import os
from PIL import Image
import numpy as np

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

# Задержка на месте перед съемкой
time.sleep(1)

# Сделать снимок с камеры
responses = client.simGetImages([
    airsim.ImageRequest("Front_Camera", airsim.ImageType.Scene, False, False)
])

# Обработка и сохранение снимка на диск
for idx, response in enumerate(responses):
    # Преобразование изображения из RAW-формата в массив NumPy
    img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)
    img_rgb = img1d.reshape(response.height, response.width, 3)

    # Преобразование массива NumPy в изображение и сохранение
    img = Image.fromarray(img_rgb)
    filename = f"photo_{idx}.png"
    img.save(os.path.join(os.getcwd(), filename))
    print(f"Снимок сохранен: {filename}")

# Приземление
client.landAsync().join()

# Отключение управления
client.armDisarm(False)
client.enableApiControl(False)

print("Полёт завершен успешно!")
