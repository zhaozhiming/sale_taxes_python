import unittest
from model.item import Item
from model.items import Items


class ItemsTestCase(unittest.TestCase):
    def setUp(self):
        item1 = Item("1 book at 12.49")
        item2 = Item("1 music CD at 14.99")
        item3 = Item("1 chocolate bar at 0.85")
        self.scenario1_items = Items([item1, item2, item3])

        item4 = Item("1 imported box of chocolates at 10.00")
        item5 = Item("1 imported bottle of perfume at 47.50")
        self.scenario2_items = Items([item4, item5])

        item6 = Item("1 imported bottle of perfume at 27.99")
        item7 = Item("1 bottle of perfume at 18.99")
        item8 = Item("1 packet of headache pills at 9.75")
        item9 = Item("1 box of imported chocolates at 11.25")
        self.scenario3_items = Items([item6, item7, item8, item9])

    def test_scenario_1_tax(self):
        self.assertEqual(self.scenario1_items.tax(), "Sales Taxes: 1.50")

    def test_scenario_1_total(self):
        self.assertEqual(self.scenario1_items.total(), "Total: 29.83")

    def test_scenario_2_tax(self):
        self.assertEqual(self.scenario2_items.tax(), "Sales Taxes: 7.65")

    def test_scenario_2_total(self):
        self.assertEqual(self.scenario2_items.total(), "Total: 65.15")

    def test_scenario_3_tax(self):
        self.assertEqual(self.scenario3_items.tax(), "Sales Taxes: 6.70")

    def test_scenario_3_total(self):
        self.assertEqual(self.scenario3_items.total(), "Total: 74.68")


if __name__ == '__main__':
    unittest.main()