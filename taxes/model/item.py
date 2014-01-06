import re
from model.tax import Tax


class Constant(object):
    COUNT_INDEX = 1
    IMPORTED_INDEX = 2
    NAME_INDEX = 3
    PRICE_INDEX = 5
    PARSE_DESCRIPTION_PATTERN = "(\d+)\s(imported\s)?(\w+(\s\w+)*)\sat\s(\d+\.\d+)"
    BOOK = ["book"]
    FOOD = ["chocolate bar", "box of chocolates"]
    BASE_TAXES = 0.1
    IMPORTED_TAXES = 0.05


class Item:
    def __init__(self, description):
        match = re.search(Constant.PARSE_DESCRIPTION_PATTERN, description)
        self.count = match.group(Constant.COUNT_INDEX)
        imported = match.group(Constant.IMPORTED_INDEX)
        self.imported = "" if imported is None else imported
        self.name = match.group(Constant.NAME_INDEX)
        self.source_price = float(match.group(Constant.PRICE_INDEX))

    def sale(self):
        return str("%s %s%s: %.2f" % (self.count, self.imported, self.name, self.price()))

    def price(self):
        return round(self.source_price * (1 + Tax(self).tax_rate()), 2)