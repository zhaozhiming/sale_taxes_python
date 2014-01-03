import unittest
from model.item import Item


class MyTestCase(unittest.TestCase):
    def test_1_book_at_12_dot_49(self):
        self.item = Item("1 book at 12.49")
        result = self.item.sale()
        self.assertEqual(result, "1 book: 12.49")

    def test_1_music_CD_at_14_dot_99(self):
        self.item = Item("1 music CD at 14.99")
        result = self.item.sale()
        self.assertEqual(result, "1 music CD: 16.49")


if __name__ == '__main__':
    unittest.main()
