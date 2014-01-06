from model.constant import Constant


class Tax:
    def __init__(self):
        pass

    def tax_rate(self, name):
        tax_rate = 0
        item_name = name.replace("imported ", "")
        if item_name not in Constant.BOOK + Constant.FOOD:
            tax_rate += Constant.BASE_TAXES
        if "imported" in name:
            tax_rate += Constant.IMPORTED_TAXES
        return tax_rate
