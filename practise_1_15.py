class Drone:
    def __init__(self, isflight, batterylevel):
        self.isflight = isflight
        self.batterylevel = batterylevel

    def takeoff(self):
        if (not self.isflight and self.batterylevel > 20):
            self.isflight = True
            print(f"Взлет разрешен. Батарея {self.batterylevel}")
            return "Дрон взлетел"
        else:
            self.isflight = False
            print(f"Взлет не разрешен. Батарея {self.batterylevel}")
            return "Дрон не взлетел"

    def land(self):
        if self.isflight:
            self.isflight = False
            return "Дрон приземлился"
        else:
            return "Дрон уже на земле"


drone1 = Drone(False, 50)
print(drone1.takeoff())
