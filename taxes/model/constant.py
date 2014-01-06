class Constant(object):
    PARSE_DESCRIPTION_PATTERN = "(\d+)\s((imported\s)?\w+(\s\w+)*)\sat\s(\d+\.\d+)"
    COUNT_INDEX = 1
    NAME_INDEX = 2
    PRICE_INDEX = 5
    BOOK = ["book"]
    FOOD = ["chocolate bar", "box of chocolates"]
    MEDICAL = ["packet of headache pills"]
    BASE_TAXES = 0.1
    IMPORTED_TAXES = 0.05
    TAX_RATE_MIN_RANGE = 0.05
    IMPORTED_TEXT_IDENTIFY = "imported"
    SALES_TAXES_TEXT_IDENTIFY = "Sales Taxes: "
    TOTAL_TEXT_IDENTIFY = "Total: "