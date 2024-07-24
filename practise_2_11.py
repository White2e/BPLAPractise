from abc import ABC, abstractmethod
import sqlite3

# паттерн абстрактная фабрика
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
            "SELECT": None,
            "FROM": None,
            "WHERE": None,
            "GROUP BY": None,
            "INSERT_INTO": None,
            "ORDER BY": None,
            "VALUES": None

        }
        self._params = []

    def select(self, table, columns="*"):
        self._query["SELECT"] = f"SELECT {columns} "
        self._query["FROM"] = f"FROM {table} "
        return self

        #  tbl_drones -> id, model, manufacturer
        #  SELECT * FROM tbl_drones WHERE manufacturer =? ORDER BY model

    def where(self, condition, parameters=None):
        if parameters:
            self._params.extend(parameters)
        self._query["WHERE"] = f"WHERE {condition}"
        return self

    def order_by(self, order):
        self._query["ORDER BY"] = f"ORDER BY {order}"
        return self

    def add_params(self, *params):
        self._params.extend(params)
        return self

    def insert_into(self, table, columns):
        # columns = ', '.join(columns)
        # columns = ["id", "model", "manufacturer"]
        # columns >>> "id, model, manufacturer"
        # ["?" for _ in columns] >>> ["?", "?", "?"]
        placeholders = ', '.join('?' for _ in columns)

        self._query["INSERT_INTO"] = f"INSERT INTO {table} ({', '.join(columns)}) "
        self._query["VALUES"] = f"VALUES ({placeholders})"

        # execute("INSERT INTO tbl_drones (id, model, manufacturer) VALUES (?,?,?)", (1, "Drone 1", "Manufacturer 1"))
        return self

    def values(self, *values):
        self._params.extend(values)
        return self

    def get_query(self):
        query = self._query.get("SELECT") or ""
        query += self._query.get("FROM") or ""
        query += self._query.get("WHERE") or ""
        query += self._query.get("GROUP BY") or ""
        query += self._query.get("INSERT_INTO") or ""
        query += self._query.get("ORDER BY") or ""

        if query.endswith(" "):
            query = query[:-1]

        if self._query.get("INSERT_INTO"):
            params = self._params
        else:
            params = tuple(self._params)

        return query, params

    def get_params(self):
        return self._params


if __name__ == "__main__":
    factory = SQLiteDBFactory()
    connection = factory.connect()
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_drones (id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, manufacturer TEXT, year INTEGER)")

    drone = {"model": "Drone 1", "manufacturer": "Manufacturer", "year": 2022}
    query_builder = QueryBuilder()
    insert_into = query_builder.insert_into("tbl_drones", ["model", "manufacturer", "year"]).values(drone["id"], drone["model"], drone["manufacturer"], drone["year"]).get_query()
    print(insert_into)
    params = query_builder.get_params()
    print(params)

    cursor.execute(*insert_into, params)
    connection.commit()

    select_query = query_builder.select("tbl_drones", ["id", ""]).get_query()
    select_params = query_builder.get_params()
    cursor.execute(*select_query, select_params)
    results = cursor.fetchall()
    for row in results:
        print(row)

    connection.close()

