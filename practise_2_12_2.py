import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_drones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    max_altitude INTEGER,
    max_speed INTEGER,
    max_flight_time INTEGER,
    serial_number TEXT UNIQUE NOT NULL,
    payload INTEGER,
    model TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    purchase_date TEXT NOT NULL,
    software_version TEXT,
    battery_capacity INTEGER,
    flight_hours INTEGER
    )
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
    )
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_drones_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    mission_id INTEGER NOT NULL,
    operator_id INTEGER NOT NULL,
    status_update_time DATETIME NOT NULL,
    battery_level INTEGER NOT NULL,
    coordinates TEXT,
    is_flying BOOLEAN DEFAULT 0,
    FOREIGN KEY (drone_id) REFERENCES tbl_drones(id),
    FOREIGN KEY (status_id) REFERENCES tbl_status(id),
    FOREIGN KEY (mission_id) REFERENCES tbl_missions(id),
    FOREIGN KEY (operator_id) REFERENCES tbl_operators(id)
    )
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_drone_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_id INTEGER NOT NULL,
    last_maintenance DATE NOT NULL,
    description TEXT,
    FOREIGN KEY (drone_id) REFERENCES tbl_drones(id)
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_drone_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    )
""")