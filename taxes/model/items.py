class Items:
    def __init__(self, items):
        self.items = items

    def tax(self):
        tax = 0
        for item in self.items:
            tax += item.tax()
        return str("Sales Taxes: %.2f" % tax)

    def total(self):
        total = 0
        for item in self.items:
            total += item.price()
        return str("Total: %.2f" % total)
