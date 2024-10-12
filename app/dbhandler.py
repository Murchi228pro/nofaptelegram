import sqlite3 as sql
from datetime import datetime as dt


class SQLHadler():

    def __init__(self, dbname: str):
        self.conn = sql.connect(dbname)
        self.cur = conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Users(
            id INT PRIMARY KEY,
            date TEXT NOT NULL
        )
        """)

    def add_user(id: int, date: str):
        self.cur.execute(
            "INSERT INTO Users (id, date) VALUES (?, ?)", (int, date))

    def update_date(id: int, date: str):
        self.cur.execute(
            "UPDATE Users SET date = ?  WHERE id = ?", (date, id))

    def delete_user(id: int):
        self.cur.execute(
            "DELETE FROM Users WHERE id = ?", (id, )
        )

    def get_user(id: int):
        self.cur.execute(
            "SELECT date FROM Users WHERE id = ?", (id, )
        )
        result = self.cur.fetchone()
        strike = (dt.now() - dt.strptime(result, "%d.%m.%Y"))
        return strike.days
