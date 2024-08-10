"""
Домашнее задание 7
Шаг 1. Реализовать паттерн Абстрактная фабрика для работы с БД. Создать интерфейс базового класса DBFactory и классы MySQLFactory, PostgreSQLFactory и др.
Шаг 2. Реализовать паттерн Строитель для создания запросов. Создать класс QueryBuilder с методами select(), where(), order_by() и др.
Шаг 3. Реализовать Отображение объектно-реляционное. Создать класс User, класс UserMapper для преобразования User в строку SQL и обратно.
Шаг 4. Реализовать паттерн Хранитель для управления соединениями с БД. Класс DBConnectionManager будет отвечать за установку, разрыв соединений.
Шаг 4. Протестировать реализованные паттерны. Создать подключения через фабрику. Построить запрос со строителем. Получить данные, преобразовать их в объекты с отображением ОР.
"""

#  Шаг 1: Реализация паттерна Абстрактная фабрика
from abc import ABC, abstractmethod


class DBFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_query_builder(self):
        pass


class MySQLFactory(DBFactory):
    def create_connection(self):
        return MySQLConnection()

    def create_query_builder(self):
        return MySQLQueryBuilder()


class MongoDBFactory(DBFactory):
    def create_connection(self):
        return MongoDBConnection()

    def create_query_builder(self):
        return MongoDBQueryBuilder()


# Классы соединений и строителей запросов
class MySQLConnection:
    def connect(self):
        print("Connecting to MySQL database...")


class MongoDBConnection:
    def connect(self):
        print("Connecting to MongoDB database...")


class MySQLQueryBuilder:
    def build_query(self):
        print("Building MySQL query...")


class MongoDBQueryBuilder:
    def build_query(self):
        print("Building MongoDB query...")


# Шаг 2: Реализация паттерна Строитель для создания запросов
class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, fields):
        self.query = f"SELECT {fields} "
        return self

    def where(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def order_by(self, field, order='ASC'):
        self.query += f"ORDER BY {field} {order} "
        return self

    def insert_into(self, table, fields, values):
        self.query = f"INSERT INTO {table} ({fields}) VALUES ({values}) "
        return self

    def get_query(self):
        return self.query.strip()


# Шаг 3: Реализация Отображение объектно-реляционное
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class UserMapper:
    def to_sql(self, user):
        return f"INSERT INTO users (id, name, email) VALUES ({user.user_id}, '{user.name}', '{user.email}')"

    def from_sql(self, record):
        user_id, name, email = record
        return User(user_id, name, email)


#  Шаг 4: Реализация паттерна Хранитель для управления соединениями с БД
class DBConnectionManager:
    def __init__(self):
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)
        connection.connect()

    def close_all(self):
        for connection in self.connections:
            print("Closing connection...")
        self.connections = []


# Тестирование реализованных паттернов
def main():
    # Шаг 1: Подключения через фабрику
    mysql_factory = MySQLFactory()
    mongo_factory = MongoDBFactory()

    mysql_connection = mysql_factory.create_connection()
    # mysql_query_builder = mysql_factory.create_query_builder()

    mongo_connection = mongo_factory.create_connection()
    # mongo_query_builder = mongo_factory.create_query_builder()

    connection_manager = DBConnectionManager()
    connection_manager.add_connection(mysql_connection)
    connection_manager.add_connection(mongo_connection)

    # Шаг 2: Строим запросы
    query_builder = QueryBuilder()
    query = query_builder.select("*").where("id=1").order_by("name").get_query()
    print("Built query:", query)
    query = query_builder.insert_into("user", "id, name, email", "1, 'Иван', 'vanya@mail.ru'").get_query()
    print("Built query:", query)

    # Шаг 3: Работа с объектно-реляционным отображением
    user = User(1, "Иван", "vanya@mail.ru")
    user_mapper = UserMapper()
    sql_query = user_mapper.to_sql(user)
    print("SQL query from user:", sql_query)
    user_from_sql = user_mapper.from_sql(("1", "Иван", "vanya@mail.ru"))
    print(f"id from SQL: {user_from_sql.user_id}, User: {user_from_sql.name}, email: {user_from_sql.email}")

    # Шаг 4: Завершение работы с соединениями
    connection_manager.close_all()

if __name__ == "__main__":
    main()

