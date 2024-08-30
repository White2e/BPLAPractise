import airsim
import cv2
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

# Транслирование видео с камеры
while True:
    # Получение изображения с передней камеры дрона
    responses = client.simGetImages([
        airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)
    ])
    response = responses[0]

    # Преобразование изображения в формат, подходящий для отображения с помощью OpenCV
    img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)  # Преобразование в одномерный массив
    img_rgb = img1d.reshape(response.height, response.width, 3)  # Преобразование в трехмерный массив (RGB изображение)


    cv2.imshow("Камера", img_rgb)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

# Приземление
client.landAsync().join()

# Отключение управления
client.armDisarm(False)
client.enableApiControl(False)

print("Полёт завершен успешно!")
