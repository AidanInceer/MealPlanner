import os
import sqlite3
from pathlib import Path


class SQLManager:
    def get_sql_file(self, sqlfilepath):
        """Get an sql query for the specified filepath.

        Args:
            sqlfilepath (str): sqlfile path.

        Returns:
            sql (str): sql query
        """
        with open(sqlfilepath) as file:
            sql = file.read()
        return sql

    def create_db(self, path):
        my_file = Path(path)
        if not my_file.is_file():
            with open(path, "x") as _:
                pass
            conn = sqlite3.connect(path)
            return conn

    def delete_db(self, path):
        my_file = Path(path)
        if my_file.is_file():
            os.remove(path)
