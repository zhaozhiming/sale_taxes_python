from model.constant import Constant
from model.tax.base_tax import BaseTax
from model.tax.imported_tax import ImportedTax
from model.tax.no_tax import NoTax


class TaxFactory:
    @staticmethod
    def build(name):
        taxes = [NoTax()]
        if TaxFactory.__item_not_in_exemptions_list(name):
            taxes.append(BaseTax())
        if TaxFactory.__item_is_imported(name):
            taxes.append(ImportedTax())
        return taxes

    @staticmethod
    def __item_not_in_exemptions_list(name):
        item_name = name.replace("%s " % Constant.IMPORTED_TEXT_IDENTIFY, "")
        return item_name not in Constant.BOOK + Constant.FOOD + Constant.MEDICAL

    @staticmethod
    def __item_is_imported(name):
        return Constant.IMPORTED_TEXT_IDENTIFY in name
