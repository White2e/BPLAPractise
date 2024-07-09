class MySingleton:
    _instance = None  # Статическое поле для хранения единственного экземпляра класса

    # данный метод вызывается ДО создания экземпляра класса
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySingleton, cls).__new__(cls)
        return cls._instance

    # данный метод вызывается ПОСЛЕ создания экземпляра класса (инициализация)
    def __init__(self):
        if MySingleton._instance is None:
            MySingleton()

    @staticmethod
    def get_instance():
        MySingleton()
        # if MySingleton._instance is None:
        #     MySingleton()
        # return MySingleton._instance


# Вызов метода get_instance дважды
singleton1 = MySingleton.get_instance()
singleton2 = MySingleton.get_instance()

# Проверка, что оба вызова возвращают один и тот же экземпляр
print(f"Идентификаторы объектов ID: {id(singleton1), id(singleton2)}, Одинаковы: {singleton1 is singleton2}")


# Создаем класс
class MyClass:
    def test(self):
        print("Метод test из MyClass вызван")


# Создаем класс - адаптер (оборачиваем MyClass)
class MyClassAdapter:
    def __init__(self, adapter):
        self.adapter = adapter  # Сохраняем экземпляр адаптируемого класса

    def call_test(self):
        self.adapter.test()  # Вызываем метод test из экземпляра MyClass


my_class = MyClass()
adapter = MyClassAdapter(my_class)
adapter.call_test()


def my_decorator(func):
    def first_func(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        return func(*args, **kwargs)
    return first_func


@my_decorator
def my_function():
    print("Выполнение my_function")


my_function()

