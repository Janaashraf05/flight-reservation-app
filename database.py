import sqlite3
from utils import resource_path

class Database:
    def __init__(self):
        self.db_path = resource_path("flights.db")
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

# Add to bottom of database.py
if __name__ == "__main__":
    import os
    db = Database()
    if os.path.exists("flights.db"):
        print("✅ Database created successfully at:", os.path.abspath("flights.db"))
    else:
        print("❌ Database creation failed")