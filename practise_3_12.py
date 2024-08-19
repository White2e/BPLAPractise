from abc import ABC, abstractmethod


class IDroneAPI(ABC):
    def __init__(self, connect_uri: None):
        self.client = None
        if connect_uri is not None:
            self.connect(connect_uri)
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def get_image(self, max_attempts=10, delay=1):
        pass

import airsim
import cv2
import numpy as np


class AirSimAPI(IDroneAPI):
    def connect(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        print("Connected to AirSim")

    def get_image(self, max_attempts=10, delay=1):
        responses = self.client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])
        if responses:
            response = responses[0]
            image_data = np.frombuffer(response.image_data_uint8, dtype=np.uint8).reshape(response.height, response.width, 3)
            cv2.imwrite('image.png', image_data)
            print('Image saved.')
        else:
            print('No images found.')

from pymavlink import mavutil
import time


class MavLinkAPI(IDroneAPI):
    def connect(self):
        print("Connecting to MavLink API")
        # Implement connecting to MavLink API
        self.client = mavutil.mavlink_connection(self.connect_uri)
        self.client.wait_heartbeat()
        print("Connected to MavLink API")

    def get_image(self, max_attempts=10, delay=1):
        """Получение изображения с камеры дрона через MAVLink"""
        # Отправка команды на захват изображения
        self.client.mav.command_long_send(
            self.client.target_system,
            self.client.target_component,
            mavutil.mavlink.MAV_CMD_IMAGE_START_CAPTURE,  # Команда для начала захвата изображения
            0,
            0,
            0,
            1,  # Количество кадров (1)
            0,
            0, 0, 0
        )

        # Ожидание получения изображения в течение нескольких попыток
        for _ in range(max_attempts):
            response = self.client.recv_match(type='CAMERA_IMAGE_CAPTURED', blocking=True, timeout=5)
            if response:
                print(f"Путь до фото: {response.file_path}")
                break
            else:
                print("Ожидание камеры...")
            time.sleep(delay)


class DroneAPIFactory:
    @staticmethod
    def get_drone_api(type_api, connect_uri):
        if type_api == 'AirSim':
            return AirSimAPI(connect_uri)
        elif type_api == 'MavLink':
            return MavLinkAPI(connect_uri)
        else:
            raise ValueError("Invalid API type")


if __name__ == '__main__':
    # Пример использования DroneAPIFactory
    type_api = 'AirSim'
    connect_uri = 'tcp://127.0.0.1:5760'
    drone = DroneAPIFactory.get_drone_api(type_api, connect_uri)
    drone.connect()
    drone.get_image()  # Получение изображения с камеры дрона

    # Пример использования AirSimAPI
    api = AirSimAPI(connect_uri='tcp://127.0.0.1:5760')
    api.connect()
    api.get_image()

    # Пример использования MavLinkAPI
    api = MavLinkAPI(connect_uri='udp://:14540')
    api.connect()
    api.get_image()