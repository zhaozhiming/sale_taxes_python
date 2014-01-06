import re
from model.constant import Constant
from model.tax_rate import TaxRate


class Item:
    def __init__(self, description):
        match = re.search(Constant.PARSE_DESCRIPTION_PATTERN, description)
        self.count = match.group(Constant.COUNT_INDEX)
        self.name = match.group(Constant.NAME_INDEX)
        self.source_price = float(match.group(Constant.PRICE_INDEX))

    def sale(self):
        return str("%s %s: %.2f" % (self.count, self.name, self.price()))

    def tax(self):
        price = round(self.source_price * TaxRate().tax_rate(self.name), 2)
        mod = price % Constant.TAX_RATE_MIN_RANGE
        return price if mod == 0 else price + (Constant.TAX_RATE_MIN_RANGE - mod)

    def price(self):
        return round(self.source_price + self.tax(), 2)
