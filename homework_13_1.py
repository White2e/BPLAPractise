import cv2
import time

# загружаем изображение с камеры БПЛА
cap = cv2.VideoCapture(0)  # используем первую подключенную камеру
ret, frame = cap.read()  # читаем кадр с камеры

if not ret:
    print("Ошибка: не удалось захватить изображение с камеры.")
    cap.release()
    exit()

# Уменьшаем разрешение изображения в 2 раза
start_time = time.time()
height, width = frame.shape[:2]
resized_frame = cv2.resize(frame, (width // 2, height // 2))

# Применяем метод Canny
edges = cv2.Canny(resized_frame, 100, 200)

# изображение в оттенки серого
gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

# Сохраняем оптимизированное изображение
cv2.imwrite("optimized_image.jpg", gray_frame)

# измеряем время обработки
end_time = time.time()
processing_time = end_time - start_time
print(f"Время обработки изображения: {processing_time:.4f} секунд")

# сравнения
cv2.imshow("Original", frame)
cv2.imshow("Small", resized_frame)
cv2.imshow("Canny", edges)
cv2.imshow("Gray", gray_frame)

# Ждем нажатия любой клавиши, затем закрываем окна
cv2.waitKey(0)
cv2.destroyAllWindows()

cap.release()
