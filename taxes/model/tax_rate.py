from model.tax_factory import TaxFactory


class TaxRate():
    def __init__(self):
        pass

    def tax_rate(self, name):
        taxes = TaxFactory.build(name)
        tax_rate = 0
        for tax in taxes:
            tax_rate += tax.tax_rate(name)
        return tax_rate