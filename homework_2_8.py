"""
Домашнее задание 8
Шаг 1. Создать интерфейс класса SomeObject с методами, предоставляющими доступ к данным.
Шаг 2. Реализовать класс Proxy, который реализует интерфейс SomeObject. В его методах добавить проверку прав доступа перед вызовом методов реального объекта.
Шаг 3. Реализовать класс SecureProxy. Также реализовать интерфейс SomeObject. В его методах добавить дополнительные проверки безопасности.
"""

from abc import ABC, abstractmethod

# Создаем абстрактный класс SomeObject
class SomeObject(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass


# Создаем реальный объект RealObject, который реализует интерфейс SomeObject
class RealObject(SomeObject):
    def __init__(self):
        self._data = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data


# Создаем прокси-класс Proxy
class Proxy(SomeObject):
    def __init__(self, real_object, user):
        self._real_object = real_object
        self._user = user

    def get_data(self):
        if self._user.has_permission("get_data"):
            return self._real_object.get_data()
        else:
            raise PermissionError("User does not have permission to get data")

    def set_data(self, data):
        if self._user.has_permission("set_data"):
            self._real_object.set_data(data)
        else:
            raise PermissionError("User does not have permission to set data")

# Создаем класс Пользователя User
class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions


# Создаем прокси-класс SecureProxy, который реализует интерфейс SomeObject с дополнительной проверкой безопасности
class SecureProxy(SomeObject):
    def __init__(self, real_object, user):
        self._real_object = real_object
        self._user = user

    def get_data(self):
        if self._user.has_permission("get_data") and self._check_security():
            return self._real_object.get_data()
        else:
            raise PermissionError("Security check failed or user does not have permission to get data")

    def set_data(self, data):
        if self._user.has_permission("set_data") and self._check_security():
            self._real_object.set_data(data)
        else:
            raise PermissionError("Security check failed or user does not have permission to set data")

    def _check_security(self):
        # Дополнительная проверка безопасности, например, проверка двухфакторной аутентификации
        # Здесь добавим пример проверки: пользователь должен быть "admin"
        return self._user.name == "admin"



# Создаем интерфейс DroneInterface
class DroneInterface(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


# Создаем реальный объект Drone и прокси-класс SecureDroneProxy
class Drone(DroneInterface):
    def fly(self):
        print("Drone is flying")

    def land(self):
        print("Drone is landing")

class SecureDroneProxy(DroneInterface):
    def __init__(self, drone, user):
        self._drone = drone
        self._user = user

    def fly(self):
        if self._check_access() and self._check_security():
            self._drone.fly()
        else:
            raise PermissionError("Access denied or security check failed")

    def land(self):
        if self._check_access() and self._check_security():
            self._drone.land()
        else:
            raise PermissionError("Access denied or security check failed")

    def _check_access(self):
        return self._user.has_permission("fly")

    def _check_security(self):
        return self._user.name == "admin"


# Запуск главной функции
def main():
    # Создаем пользователя и проверяем права доступа
    user1 = User("admin", ["get_data", "set_data", "fly"])
    user2 = User("guest", ["get_data"])

    # Создаем реальный объект и прокси
    real_object = RealObject()
    proxy = Proxy(real_object, user1)
    secure_proxy = SecureProxy(real_object, user1)

    # Работа с данными через прокси
    proxy.set_data("some data")
    print(proxy.get_data())

    try:
        secure_proxy.set_data("secure data")
        print(secure_proxy.get_data())
    except PermissionError as e:
        print(e)

    # Работа с беспилотником через прокси
    drone = Drone()
    secure_drone_proxy = SecureDroneProxy(drone, user1)
    secure_drone_proxy.fly()
    secure_drone_proxy.land()

    try:
        secure_drone_proxy = SecureDroneProxy(drone, user2)
        secure_drone_proxy.fly()
    except PermissionError as e:
        print(e)

if __name__ == "__main__":
    main()
