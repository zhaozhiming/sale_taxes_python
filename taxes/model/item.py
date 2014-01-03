import re

PARSE_DESCRIPTION_PATTERN = "(\d+)\s(\w+(\s\w+)*)\sat\s(\d+\.\d+)"
BOOK = ["book"]


class Item:
    def __init__(self, description):
        self.description = description
        match = re.search(PARSE_DESCRIPTION_PATTERN, self.description)
        self.count = match.group(1)
        self.name = match.group(2)
        self.price = match.group(4)
        if self.name not in BOOK:
            self.price = round(float(self.price) * 1.1, 2)

    def sale(self):
        return self.count + " " + self.name + ": " + str(self.price)