#from dji_sdk import *
from pymavlink import mavutil


class Drone:
    def __init__(self, connect_url):
        self.master = mavutil.mavlink_connection(connect_url)
        self.master.wait_heartbeat()
        print("Connected to Drone")

    def arm(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,  # Confirmation flag
            1,  # Arm
            0, 0, 0, 0, 0, 0  # Parameters
        )
        print("Drone Armed")

    def disarm(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,  # Confirmation flag
            0,  # Disarm
            0, 0, 0, 0, 0, 0  # Parameters
        )
        print("Drone Disarmed")

    def takeoff(self, altitude):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0,  # Confirmation flag
            0,  # Disarm
            0, 0, 0, 0, 0, altitude  # Parameters
        )
        print(f"Drone takeoff: {altitude}")

    def land(self):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_LAND,
            0,  # Confirmation flag
            0,  #
            0, 0, 0, 0, 0, 0  # Parameters
        )
        print(f"Drone land")

    def fly_to(self, latitude, longitude, altitude):
        self.master.mav.command_long_send(
            self.master.target_system,
            self.master.target_component,
            0,  # Confirmation flag
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            0, 0,
            0, 0, 0,
            # Latitude, longitude, altitude
            latitude, longitude, altitude  # Parameters
        )
        print(f"Drone fly to: {latitude}, {longitude}, {altitude}")


def main():
    drone = Drone('udp:127.0.0.1:14550')
    drone.arm()
    drone.takeoff(10)
    drone.fly_to(37.7749, -122.4194, 10)
    drone.land()
    drone.disarm()


if __name__ == "__main__":
    main()

