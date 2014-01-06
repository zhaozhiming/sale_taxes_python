from abc import abstractmethod
from model.constant import Constant


class TaxRate():
    def __init__(self):
        pass

    def tax_rate(self, name):
        tax_rate = 0
        if self.item_not_in_exemptions_list(name):
            tax_rate += Constant.BASE_TAXES
        if self.item_is_imported(name):
            tax_rate += Constant.IMPORTED_TAXES
        return tax_rate

    @abstractmethod
    def item_not_in_exemptions_list(self, name):
        item_name = name.replace("%s " % Constant.IMPORTED_TEXT_IDENTIFY, "")
        return item_name not in Constant.BOOK + Constant.FOOD + Constant.MEDICAL

    @abstractmethod
    def item_is_imported(self, name):
        return Constant.IMPORTED_TEXT_IDENTIFY in name
