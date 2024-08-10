# Фабричный метод
from abc import ABC, abstractmethod


class Mission(ABC):
    @abstractmethod
    def execute(self):
        pass


class BackMission(Mission):
    def execute(self):
        return "Return to base"


class MappingMission(Mission):
    def execute(self):
        return "Run cartography"


class PatrolMission(Mission):
    def execute(self):
        return "Patrol mission"


class FireFlightMission(Mission):
    def execute(self):
        return "Fire flight"


class EvacuationMission(Mission):
    def execute(self):
        return "Evacuation mission"


class FollowingMission(Mission):
    def execute(self):
        return "Folloving mission"


class MissionFactory(ABC):
    @abstractmethod
    def create_mission(self):
        pass


class BackMissionFactory(MissionFactory):
    def create_mission(self):
        return BackMission()


class MappingMissionFactory(MissionFactory):
    def create_mission(self):
        return MappingMission()


class PatrolMissionFactory(MissionFactory):
    def create_mission(self):
        return PatrolMission()


class EvacuationMissionFactory(MissionFactory):
    def create_mission(self):
        return EvacuationMission()


class FollowingMissionFactory(MissionFactory):
    def create_mission(self):
        return FollowingMission()


class FireFlightMissionFactory(MissionFactory):
    def create_mission(self):
        return FireFlightMission()


def mission_planner(factory: MissionFactory):
    mission = factory.create_mission()
    return mission.execute()


patrol_factory = MappingMissionFactory()
print((mission_planner(patrol_factory)))

mapping_factory = MappingMissionFactory()
print((mission_planner(mapping_factory)))
