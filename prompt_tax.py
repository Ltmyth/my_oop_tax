import tax_class as p

gross = int(input("Please enter gross amount:"))
tax = float(input("Please tax rate:"))

x = p.Tax(gross_income=gross, tax_rate=tax)
print(x)
