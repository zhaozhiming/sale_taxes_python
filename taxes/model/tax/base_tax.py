from model.constant import Constant
from model.tax.no_tax import NoTax


class BaseTax(NoTax):
    def tax_rate(self, name):
        return Constant.BASE_TAXES