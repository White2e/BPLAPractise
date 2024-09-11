import cv2
import time

# Шаг 1: Импортируем библиотеку OpenCV и загружаем изображение с камеры БПЛА
cap = cv2.VideoCapture(0)  # используем первую подключенную камеру
ret, frame = cap.read()  # читаем кадр с камеры

if not ret:
    print("Ошибка: не удалось захватить изображение с камеры.")
    cap.release()
    exit()

# Шаг 2: Уменьшаем разрешение изображения в 2 раза
start_time = time.time()
height, width = frame.shape[:2]
resized_frame = cv2.resize(frame, (width // 2, height // 2))

# Шаг 3: Применяем метод Canny для выделения контуров
edges = cv2.Canny(resized_frame, 100, 200)

# Шаг 4: Переводим изображение в оттенки серого
gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

# Шаг 5: Сохраняем оптимизированное изображение и измеряем время обработки
cv2.imwrite("optimized_image.jpg", gray_frame)

end_time = time.time()
processing_time = end_time - start_time
print(f"Время обработки изображения: {processing_time:.4f} секунд")

# Выводим оригинальное и обработанное изображение для сравнения
cv2.imshow("Оригинальное изображение", frame)
cv2.imshow("Уменьшенное изображение", resized_frame)
cv2.imshow("Контуры (Canny)", edges)
cv2.imshow("Оттенки серого", gray_frame)

# Ждем нажатия любой клавиши, затем закрываем окна
cv2.waitKey(0)
cv2.destroyAllWindows()

cap.release()
