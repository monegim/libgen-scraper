import os
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

    def test_get_image_location(self):
        book_id = 3139992
        location = helpers.get_image_location(self.conn, book_id)
        self.assertEqual('2022/7', location)

    def test_save_thumbnail_when_dir_does_not_exist(self):
        book_id = "3139992"
        image_location = helpers.get_image_location(self.conn, book_id)
        image_url = "https://libgen.is/covers/3139000/c3603c11006024805e0e526df6de29c2-g.jpg"
        base_location = 'files/thumbnails'
        location = os.path.join(base_location, image_location)
        helpers.save_thumbnail(image_url, book_id, location)

    def test_check_if_image_exists(self):
        book_id = "3139992"
        base_location = 'files/thumbnails'
        extension = 'jpg'
        self.assertTrue(helpers.check_if_image_exists(
            self.conn, base_location, book_id, extension))


if __name__ == '__main__':
    unittest.main()
