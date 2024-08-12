from pymavlink import mavutil

class Drone:
    def __init__(self, connect_uri):
        self.master = mavutil.mavlink_connection(connect_uri)
        self.master.wait_heartbeat()
        print("Соединение с дроном установлено")

    def arm(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1, 0, 0, 0, 0, 0, 0
        )
        print("Армирование дрона завершено")

    def disarm(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            0, 0, 0, 0, 0, 0, 0
        )
        print("Двигатели дрона заблокированы")


    def takeoff(self, altitude):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0,
            0, 0, 0, 0, 0, 0, altitude
        )
        print(f"Взлет на высоту {altitude} м")

    def fly_to(self, latitude, longitude, altitude):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            0,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            0, 0,
            0, 0, 0,
            latitude, longitude, altitude
        )
        print(f"летим к точке: {latitude, longitude, altitude}")

    def land(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_LAND,
            0,
            0, 0, 0, 0, 0, 0, 0
        )
        print(f"Дрон приземлился")


if __name__ == '__main__':
    drone_1 = Drone("udp:127.0.0.1:14550")
    drone_1.arm()
    drone_1.takeoff(10)
    latitude, longitude, altitude = 40.4444, 50.5555, 10
    drone_1.fly_to(latitude, longitude, altitude)
    drone_1.land()
    drone_1.disarm()



