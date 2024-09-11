#  тестирование приложения
#
import unittest
from practise_1_15 import Drone


class TestDrone(unittest.TestCase):
    def setUp(self):
        self.drone = Drone(False, 100)

    def test_takeoff(self):
        # hight level battery
        self.drone.batterylevel = 50
        result = self.drone.takeoff()
        self.assertTrue(self.drone.isflight)
        self.assertEqual(result, "Дрон взлетел")

        # low battery level
        self.drone.batterylevel = 10
        result = self.drone.takeoff()
        self.assertTrue(not self.drone.isflight)
        self.assertEqual(result, "Дрон не взлетел")

    def test_land_not_flying(self):
        self.drone.isflight = False
        result = self.drone.land()
        self.assertFalse(self.drone.isflight)
        self.assertEqual(result, "Дрон уже на земле")

    def test_land_not_flying(self):
        self.drone.isflight = True
        result = self.drone.land()
        self.assertFalse(self.drone.isflight)
        self.assertEqual(result, "Дрон приземлился")


if __name__ == "__main__":
    unittest.main()
