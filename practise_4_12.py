import airsim
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

async def get_telemetry(client):
    """Получение телеметрии с дрона"""
    while True:
        telemetry = await client.getMultirotorStateAsync()
        position = telemetry.kinematics_estimated.position
        velocity = telemetry.kinematics_estimated.linear_velocity
        info_state = f"""Drone position:
                         x = {position.x_val:.2f},
                         y = {position.y_val:.2f},
                         z = {position.z_val:.2f} m
                         Velocity (m/s):
                         x = {velocity.x_val:.2f},
                         y = {velocity.y_val:.2f},
                         z = {velocity.z_val:.2f} m
                    """
        logging.info(f"State: {info_state}")
        await asyncio.sleep(1)


async def mission_test(client: airsim.MultirotorClient):
    waypoints = [
        airsim.Vector3r(0, 0, -10),    # Up
        airsim.Vector3r(10, 0, -10),   # Forward
        airsim.Vector3r(0, 10, -10),   # Right
        airsim.Vector3r(-10, -10, -10),  # назад по диагонали
        airsim.Vector3r(0, 0, -5)     # Up
    ]

    velocity = 5

    for waypoint in waypoints:
        client.moveToPositionAsync(waypoint.x_val, waypoint.y_val, waypoint.z_val, velocity).join()
        await asyncio.sleep(1)

    await manual_control(client)

    #client.landAsync().join()
    await landed(client)


async def manual_control(client: airsim.MultirotorClient):
    """Контроль дрона вручную"""
    remote_control_data = airsim.RCData(pitch=0.5, roll=0.0, yaw=0.0, throttle=0.5, is_initialized=True, is_valid=True)
    client.moveByRCAsync(remote_control_data)
    await asyncio.sleep(1)
    await landed(client)


async def landed(client):
    """ тут код из кода учителя"""


    # """Обработать событие приземления."""
    # # Даем дрону немного времени для стабилизации
    # self.client.hoverAsync().join()
    # time.sleep(2)
    #
    # # После зависания снова включаем управление API для следующего этапа полета
    # self.client.enableApiControl(True)
    #
    # z = self.client.getMultirotorState().kinematics_estimated.position.z_val
    #
    # # Если высота выше 5, опускаемся до 5
    # if z < -5:
    #     logging.info("Снижаемся")
    #     self.client.moveToPositionAsync(0, 0, -5, 5).join()
    #     time.sleep(2)
    #
    # # Садимся на землю
    # logging.info("Посадка...")
    # self.client.landAsync().join()

    # Блокируем дрон после завершения миссии
    logging.info("Дрон заблокирован.")
    self.client.armDisarm(False)
    self.client.enableApiControl(False)


async def main():
    # Подключение к симулятору
    client = airsim.MultirotorClient()
    client.confirmConnection()

    # Разблокировка управления и взлет
    client.enableApiControl(True)
    client.armDisarm(True)

    client.takeoffAsync().join()

    # Запуск потока для получения телеметрии
    await asyncio.gather(get_telemetry(client))
    client.armDisarm(False)
    client.enableApiControl(False)


if __name__ == '__main__':
    asyncio.run(main())


    # Взлет до высоты 3 метра
    # await client.moveOnPathAsync([
    #     airsim.Vector3rpy(0, 0, 0),  # начальная позиция
    #     airsim.Vector3rpy(0, 0, 0),  # первый угол поворота
    #     airsim.Vector3rpy(0, 0, 0),  # второй угол поворота
    #     airsim.Vector3rpy(0, 0, 30),  # третий угол