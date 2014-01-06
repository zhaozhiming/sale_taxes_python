class Items:
    def __init__(self, items):
        self.items = items

    def tax(self):
        total = 0
        for item in self.items:
            total += item.tax
        return str("Sales Taxes: %.2f" % total)
