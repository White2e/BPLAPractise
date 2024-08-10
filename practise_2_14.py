from abc import ABC, abstractmethod


class DroneRepository(ABC):
    @abstractmethod
    def get_all_drones(self):
        #  Получить список всех дронов
        return list(self.drones.values())

    @abstractmethod
    def get_drone_by_id(self, drone_id: int):
        return self.drones.get(drone_id, None)

    @abstractmethod
    def update_drone_status(self, drone_id: int, new_status: str):
        # Обновить статус дрона по указанному идентификатору
        # new_status - новый статус дрона ('active', 'inactive', 'charging')
        if id in self.drones:
            self.drones[drone_id]['status'] = new_status
        pass

    @abstractmethod
    def add_drone(self, drone_id: dict):
        # Добавить дрон по указанному идентификатору
        id = drone_id['id']
        self._drones[id] = drone_id


    @abstractmethod
    def remove_drone(self, drone_id: int):
        # Удалить дрон по указанному идентификатору
        del self.drones[drone_id]

def list_all_drones(drone_repository: DroneRepository):
    drones = drone_repository.get_all_drones()
    for drone in drones:
        print(f"ID: {drone['id']}, Модель: {drone['model']}, Статус: {drone['status']}")

if __name__ == "__main__":
    drone_repository = MemoryDroneRepository()
    drone_repository.add_drone({
        'id': 1,
        'model': 'Drone 1',
        'status': 'active'
    })
    drone_repository.add_drone({
        'id': 2,
        'model': 'Drone 2',
        'status': 'inactive'
    })
    drone_repository.list_drones(drone_repository)

    drone_repository.update_drone_status(1, 'charging')
    drone_repository.list_drones(drone_repository)

    drone_repository.remove_drone(2)
    drone_repository.list_drones(drone_repository)