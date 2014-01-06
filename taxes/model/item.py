import re


class Constant(object):
    COUNT_INDEX = 1
    NAME_INDEX = 2
    PRICE_INDEX = 4
    PARSE_DESCRIPTION_PATTERN = "(\d+)\s(\w+(\s\w+)*)\sat\s(\d+\.\d+)"
    BOOK = ["book"]
    FOOD = ["chocolate bar"]


class Item:
    def __init__(self, description):
        match = re.search(Constant.PARSE_DESCRIPTION_PATTERN, description)
        self.count = match.group(Constant.COUNT_INDEX)
        self.name = match.group(Constant.NAME_INDEX)
        self.price = price = round(float(match.group(Constant.PRICE_INDEX)), 2)

        self.tax = 0
        if self.name not in Constant.BOOK + Constant.FOOD:
            self.price = round(price * 1.1, 2)
            self.tax = round(price * 0.1, 2)

    def sale(self):
        return str("%s %s: %.2f" % (self.count, self.name, self.price))