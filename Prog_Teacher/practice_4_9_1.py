
import subprocess

# Указываем путь к устройству видеозахвата (в Linux это может быть /dev/video0)
video_device = "/dev/video0"

# Параметры для видеопотока
rtmp_url = "rtmp://your_server_ip:port/live/stream_name"  # Адрес RTMP сервера
video_codec = "libx264"  # Используемый кодек
bitrate = "1000k"  # Битрейт видеопотока
resolution = "1280x720"  # Разрешение видеопотока
framerate = "30"  # Частота кадров

# Команда FFmpeg для захвата и передачи видеопотока
ffmpeg_command = [
    "ffmpeg",
    "-f", "v4l2",  # Формат видеозахвата
    "-i", video_device,  # Входное устройство
    "-c:v", video_codec,  # Кодек видео
    "-b:v", bitrate,  # Битрейт
    "-s", resolution,  # Разрешение
    "-r", framerate,  # Частота кадров
    "-f", "flv",  # Формат выходного потока (RTMP требует FLV)
    rtmp_url  # URL RTMP сервера
]

# Запуск FFmpeg через subprocess
process = subprocess.Popen(ffmpeg_command)

try:
    # Ожидаем завершения процесса (например, после остановки потока)
    process.communicate()
except KeyboardInterrupt:
    # Останавливаем процесс при нажатии Ctrl+C
    process.terminate()
