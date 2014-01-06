BOOK = ["book"]
FOOD = ["chocolate bar", "box of chocolates"]
BASE_TAXES = 0.1
IMPORTED_TAXES = 0.05


class Tax:
    def __init__(self, item):
        self.item = item

    def tax_rate(self):
        imported = self.item.imported
        name = self.item.name
        tax_rate = 0
        if name not in BOOK + FOOD:
            tax_rate += BASE_TAXES
        if "imported" in imported:
            tax_rate += IMPORTED_TAXES
        return tax_rate
