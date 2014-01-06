from model.constant import Constant


class TaxRate:
    def __init__(self):
        pass

    def tax_rate(self, name):
        tax_rate = 0
        item_name = name.replace("%s " % Constant.IMPORTED_TEXT_IDENTIFY, "")
        if item_name not in Constant.BOOK + Constant.FOOD + Constant.MEDICAL:
            tax_rate += Constant.BASE_TAXES
        if Constant.IMPORTED_TEXT_IDENTIFY in name:
            tax_rate += Constant.IMPORTED_TAXES
        return tax_rate
