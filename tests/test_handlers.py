import unittest
from scripts import db


class TestdbModule(unittest.TestCase):
    def setUp(self) -> None:
        self.database_path = 'files/database.db'
        self.conn = db.sql_connection(self.database_path)
