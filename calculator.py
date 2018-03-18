#!/usr/bin/env python3
import sys
salary = 0
tax_income = 0
tax_pay = 0
try:
    salary = int(sys.argv[1])
except:
    print("Parameter Error")

tax_income = salary - 0 - 3500

if tax_income > 0 and tax_income < 1500:
    tax_pay = tax_income * 0.03 - 0
elif tax_income > 1500 and tax_income < 4500:
    tax_pay = tax_income * 0.1 - 105
elif tax_income > 4500 and tax_income < 9000:
    tax_pay = tax_income * 0.2 - 555
elif tax_income > 9000 and tax_income < 35000:
    tax_pay = tax_income * 0.25 - 1005
elif tax_income > 35000 and tax_income < 55000:
    tax_pay = tax_income * 0.3 - 2755
elif tax_income > 55000 and tax_income < 80000:
    tax_pay = tax_income * 0.35 - 5505
elif tax_income > 80000:
    tax_pay = tax_income * 0.4 - 13505

print(format(tax_pay,".2f"))
