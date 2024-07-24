class Tax:
    def __init__(self,gross_income, tax_rate):
        self.gross_income = gross_income
        self.tax_rate = tax_rate

    def tax(self):
        rate = self.tax_rate/100
        tax_amount = int(self.gross_income*rate)
        return tax_amount

    def net_income(self):
        net_income = self.gross_income - self.tax()
        return int(net_income)

    def __str__(self):
        tax_info = f"{self.tax_rate} % TAX on : UGX {self.gross_income} is : UGX {self.tax()}."
        income_info = f"And the NET income is : UGX {self.net_income()}."
        print(tax_info)
        return income_info


