import unittest
from scripts import db


class TestdbModule(unittest.TestCase):
    def setUp(self) -> None:
        self.database_path = 'files/database.db'
        self.conn = db.sql_connection(self.database_path)

    def test_sql_read_query(self):
        book_id = 3139992
        rows = db.sql_read_query(self.conn, "BOOK_ID", book_id)
        self.assertEqual(rows[0]['id'], 4)

    def test_sql_read_query_none(self):
        book_id = 3
        rows = db.sql_read_query(self.conn, "BOOK_ID", book_id)
        print(rows)
        self.assertEqual(rows, [])


if __name__ == '__main__':
    unittest.main()
