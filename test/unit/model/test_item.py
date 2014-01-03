
import unittest
from model.item import Item


class MyTestCase(unittest.TestCase):

    def test_1_book_at_12_dot_49(self):
        self.item = Item("1 book at 12.49")

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
