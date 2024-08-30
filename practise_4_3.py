import concurrent.futures
import cv2
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
stop_flag = False

class Drone:
    def __init__(self):
        self.__obstacle_detected = False
        self.__altitude = 0

    def update_altitude(self, new_altitude):
        self.__altitude = new_altitude

    def update_detected(self, status):
        self.__obstacle_detected = status

    def control(self):
        if self.__obstacle_detected:
            logging.info('Drone is avoiding obstacle')
        elif self.__altitude < 10:
            logging.info('Drone is taking off')
            self.update_altitude(self.__altitude + 1)
        else:
            logging.info('Drone is flying')


def read_altimeter(drone: Drone):
    global stop_flag
    while not stop_flag:
        altitude = random.uniform(5.0, 15.0)
        drone.update_altitude(altitude)
        logging.info(f'Current altitude: {altitude:.2f} meters')
        time.sleep(0.01)


def control(drone: Drone):
    global stop_flag
    while not stop_flag:
        drone.control()
        time.sleep(0.1)


def read_video(drone: Drone):
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
            drone.update_detected(True)
        else:
            drone.update_detected(False)

        cv2.imshow('Video obstacle', edges)
        if (cv2.getWindowProperty('Obstacle detected', cv2.WND_PROP_VISIBLE) < 1 or
            cv2.waitKey(1) & 0xFF == ord('q')):
            logging.info('Obstacle detected, stopping drone')
            stop_flag = True
            break

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        # if drone.__obstacle_detected:
        #     logging.info('Obstacle detected, stopping drone')
        #     stop_flag = True

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    drone = Drone()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        altimeter_futures = executor.submit(read_altimeter, drone)
        control_future = executor.submit(control, drone)
        video_future = executor.submit(read_video, drone)

        concurrent.futures.wait([video_future, altimeter_futures, control_future])

