import concurrent.futures
import cv2
import time
import random
import logging
#import airsim
import numpy as np
from pyinstrument import Profiler

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
stop_flag = False


class Lidar:
    def __init__(self, client):
        self.__client = client
        self.__lidar = None
        self.debug = False

    def update(self):
        if self.debug:
            with open("lidar.txt", "r") as file:
                self.__lidar = file.read()
            return
        self.__lidar = self.__client.getLidarData()

    def get_lidar_data(self):
        # Simulate reading lidar data
        self.update()
        return self.__lidar

    def filter_front(self):
        # x - горизонтальная ось
        # y - глубина
        # z - вертикальная ось
        y_min, y_max = (0, 10)  # еще успеем увернуться
        z_min, z_max = (-2, 2)
        x_min, x_max = (-4, 4)
        if self.__debug:
            points = np.array(self.__lidar.split(' '), dtype=float).reshape(-1, 3)
        else:
            points = np.array(self.__lidar.point_cloud).reshape(-1, 3)
        filter_points = points[
            (points[:, 0] >= x_min) & (points[:, 0] <= x_max) &
            (points[:, 1] >= y_min) & (points[:, 1] <= y_max) &
            (points[:, 2] >= z_min) & (points[:, 2] <= z_max)
        ]
        return filter_points


class Drone:
    def __init__(self):
        self.__obstacle_detected = False
        self.debug = False
        self.status_camera = None
        self.status_lidar = None
        self.lidar = None

    def set_lidar(self, lidar):
        self.lidar = lidar

    def connect(self):
        if self.debug:
            logging.info("Debug mode. Not connected")
            return
        self.__client = airsim.MultirotorClient()
        self.__client.confirmConnection()

    def update_altitude(self, new_altitude):
        self.__altitude = new_altitude

    def update_detected(self, status_camera=None, status_lidar=None):
        if status_camera is not None:
            status_lidar = self.status_lidar
        elif status_lidar is not None:
            status_camera = self.status_camera

        self.__obstacle_detected = status_camera or status_lidar

        self.status_camera = status_camera
        self.status_lidar = status_lidar

    def control(self):
        if self.__obstacle_detected:
            logging.info('Drone is avoiding obstacle')
        elif self.__altitude < 10:
            logging.info('Drone is taking off')
            self.update_altitude(self.__altitude + 1)
        else:
            logging.info('Drone is flying')


def check_lidar(drone: Drone):
    profile = Profiler()
    profile.start()
    global stop_flag
    while not stop_flag:
        drone.lidar.update()
        if len(drone.lidar.filter_front()) > 0:
            logging.info("Lidar is avoiding obstacle")
            drone.update_detected(status_lidar=True)
        else:
            drone.update_detected(status_lidar=False)
        time.sleep(1)
    profile.stop()
    profile.print()


def read_altimeter(drone: Drone):
    profile = Profiler()
    profile.start()
    global stop_flag
    while not stop_flag:
        altitude = random.uniform(5.0, 15.0)
        drone.update_altitude(altitude)
        logging.info(f'Current altitude: {altitude:.2f} meters')
        time.sleep(0.1)
    profile.stop()
    profile.print()


def control(drone: Drone):
    profile = Profiler()
    profile.start()
    global stop_flag
    while not stop_flag:
        drone.control()
        time.sleep(0.1)
    profile.stop()
    profile.print()


def read_video(drone: Drone):
    profile = Profiler()
    profile.start()
    global stop_flag
    logging.info('Starting video capture')
    cap = cv2.VideoCapture(0)
    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            logging.error('Error reading video frame')
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        if edges.sum() > 100000:
            logging.info("Camera detected obstacle")
            drone.update_detected(True)
        else:
            drone.update_detected(False)

        cv2.imshow('Video obstacle', edges)
        if (cv2.getWindowProperty('Obstacle detected', cv2.WND_PROP_VISIBLE) < 1 or
            cv2.waitKey(1) & 0xFF == ord('q')):
            logging.info('Obstacle detected, stopping drone')
            stop_flag = True
            break

        time.sleep(0.05)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        # if drone.__obstacle_detected:
        #     logging.info('Obstacle detected, stopping drone')
        #     stop_flag = True

    cap.release()
    cv2.destroyAllWindows()
    profile.stop()
    profile.print()
    #exit()


if __name__ == '__main__':
    lidar = Lidar(None)
    lidar.debug = True
    #logging.info(lidar.get_lidar_data())  # comment
    #logging.info(lidar.filter_front())    #

    drone = Drone()
    drone.set_lidar(lidar)

    #profile = Profiler()
    #profile.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        altimeter_futures = executor.submit(read_altimeter, drone)
        control_future = executor.submit(control, drone)
        video_future = executor.submit(read_video, drone)
        lidar_future = executor.submit(check_lidar, drone)

        concurrent.futures.wait([video_future, altimeter_futures, control_future, lidar_future])

    #profile.stop()
    #profile.print()
