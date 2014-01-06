import unittest
from model.item import Item
from model.items import Items


class ItemsTestCase(unittest.TestCase):
    def test_scenario_1_tax(self):
        item1 = Item("1 book at 12.49")
        item2 = Item("1 music CD at 14.99")
        item3 = Item("1 chocolate bar at 0.85")
        self.items = Items([item1, item2, item3])
        self.assertEqual(self.items.tax(), "Sales Taxes: 1.50")

    def test_scenario_1_total(self):
        item1 = Item("1 book at 12.49")
        item2 = Item("1 music CD at 14.99")
        item3 = Item("1 chocolate bar at 0.85")
        self.items = Items([item1, item2, item3])
        self.assertEqual(self.items.total(), "Total: 29.83")


if __name__ == '__main__':
    unittest.main()