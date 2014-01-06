import re

PARSE_DESCRIPTION_PATTERN = "(\d+)\s(\w+(\s\w+)*)\sat\s(\d+\.\d+)"
BOOK = ["book"]
FOOD = ["chocolate bar"]


class Item:
    def __init__(self, description):
        self.description = description
        match = re.search(PARSE_DESCRIPTION_PATTERN, self.description)
        self.count = match.group(1)
        self.name = match.group(2)
        self.price = match.group(4)
        self.tax = 0
        if self.name not in BOOK + FOOD:
            self.price = round(float(match.group(4)) * 1.1, 2)
            self.tax = round(float(match.group(4)) * 0.1, 2)


    def sale(self):
        return self.count + " " + self.name + ": " + str("%.2f" % self.price)