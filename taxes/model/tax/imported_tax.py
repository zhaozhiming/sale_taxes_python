from model.constant import Constant
from model.tax.no_tax import NoTax


class ImportedTax(NoTax):
    def tax_rate(self, name):
        return Constant.IMPORTED_TAXES