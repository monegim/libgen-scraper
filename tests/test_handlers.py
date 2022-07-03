import unittest
from scripts import db, helpers


class TestdbModule(unittest.TestCase):
    def setUp(self) -> None:
        self.database_path = 'files/database.db'
        self.conn = db.sql_connection(self.database_path)

    def test_get_image_extension(self):
        url = "/covers/2343000/a5c884facc5623ce320b1d947b6bdc92-d.jpg"
        ext = helpers.get_image_extension(url)
        self.assertEqual('jpg', ext)

    def test_save_thumbnail_when_dir_does_not_exist(self):
        pass


if __name__ == '__main__':
    unittest.main()
