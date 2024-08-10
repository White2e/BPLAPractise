from abc import ABC, abstractmethod
import sqlite3

# паттерн Абстрактная фабрика
class DBFactory(ABC):
    @abstractmethod
    def connect(self):
        pass


class SQLiteDBFactory(DBFactory):
    def connect(self):
        return sqlite3.connect(':memory:')


# паттерн Строитель
class QueryBuilder:
    def __init__(self):
        self._query = {
            "select": None,
            "from": None,
            "where": None,
            "order_by": None,
            "insert_into": None,
            "values": None
        }

        self._prams = []

    def select(self, table, columns="*"):
        self._query["select"] = f"SELECT {columns} "
        self._query["from"] = f"FROM {table} "
        return self

        # tbl_drones -> id, model, manufacturer
        # SELECT * FROM tbl_drones
        # SELECT manufacturer FROM tbl_drones

    def where(self, condition, parametrs=None):
        self._query["where"] = f"WHERE {condition} "
        if parametrs:
            self._prams.extend(parametrs)
        return self

    def order_by(self, order):
        self._query["order_by"] = f"ORDER BY {order}"
        return self

    def add_params(self, *parametrs):
        self._prams.extend(parametrs)
        return self

    def insert_into(self, table, columns):
        cols = ",".join(columns)
        # columns = ["model", "manufacturer"]
        # cols = ",".join(columns)
        # cols >>> "model,manufacturer"
        placeholders = ",".join(["?"] * len(columns))
        self._query["insert_into"] = f"INSERT INTO {table} ({cols})"
        self._query["values"] = f"VALUES ({placeholders})"

        # INSERT INTO название_таблицы (список_столбцов) VALUES (значения_столбцов);
        # INSERT INTO tbl_drones (model, manufacturer) VALUES ("model x", "FlyCorp")
        # execute("INSERT INTO tbl_drones (model, manufacturer) VALUES (?, ?)", ("model x", "FlyCorp"))
        return self

    def values(self, *values):
        self._prams.extend(values)
        return self

    def get_query(self):
        query = ""
        if self._query["select"]:
            query = f"{self._query['select']} {self._query['from']}"
        if self._query["where"]:
            query += f" {self._query['where']}"
        if self._query["order_by"]:
            query += f" {self._query['order_by']}"
        if self._query["insert_into"]:
            query = f"{self._query['insert_into']} {self._query['values']}"
        return query

    def get_params(self):
        return self._prams


if __name__ == "__main__":
    sql = SQLiteDBFactory()
    connection = sql.connect()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE tbl_drones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        manufacturer TEXT,
        year INTEGER
    )
    """)

    drone = {
        "model": "Model X",
        "manufacturer": "SkyCorp",
        "year": 2024,
    }

    query_builder = QueryBuilder()
    insert_into = query_builder.insert_into("tbl_drones", ["model", "manufacturer", "year"]).values(drone["model"],
                                                                                                    drone[
                                                                                                        "manufacturer"],
                                                                                                    drone[
                                                                                                        "year"]).get_query()
    print(insert_into)
    params = query_builder.get_params()
    cursor.execute(insert_into, params)
    connection.commit()

    select_query = QueryBuilder()
    select_query = select_query.select("tbl_drones").get_query()
    cursor.execute(select_query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    connection.close()













