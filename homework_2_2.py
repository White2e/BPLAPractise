from abc import ABC, abstractmethod


#  Паттерн Наблюдатель
class MyObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class MySubject:
    def __init__(self):
        self._observers = []

    def register(self, observer: MyObserver):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


#  паттерн Итератор
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# Пример использования
data = [1, 2, 3, 4, 5]
my_iterator = MyIterator(data)

for item in my_iterator:
    print(item)


#  паттерн шаблонный метод
class MyBase(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass


class MyClass1(MyBase):
    def step1(self):
        print("MyClass1: Реализация шага 1")

    def step2(self):
        print("MyClass1: Реализация шага 2")

    def step3(self):
        print("MyClass1: Реализация шага 3")


class MyClass2(MyBase):
    def step1(self):
        print("MyClass2: Реализация шага 1")

    def step2(self):
        print("MyClass2: Реализация шага 2")

    def step3(self):
        print("MyClass2: Реализация шага 3")


# Пример использования
instance1 = MyClass1()
instance2 = MyClass2()

print("Вызов template_method для MyClass1:")
instance1.template_method()

print("\nВызов template_method для MyClass2:")
instance2.template_method()
