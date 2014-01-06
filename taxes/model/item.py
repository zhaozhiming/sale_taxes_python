import re
from model.constant import Constant
from model.tax import Tax


class Item:
    def __init__(self, description):
        match = re.search(Constant.PARSE_DESCRIPTION_PATTERN, description)
        self.count = match.group(Constant.COUNT_INDEX)
        self.name = match.group(Constant.NAME_INDEX)
        self.source_price = float(match.group(Constant.PRICE_INDEX))

    def sale(self):
        return str("%s %s: %.2f" % (self.count, self.name, self.price()))

    def price(self):
        return round(self.source_price * (1 + Tax().tax_rate(self.name)), 2)