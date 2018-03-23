#!/usr/bin/env python3
import sys
arg_list = []
idnum = 0
salary = 0 
tax_income = 0 
tax_pay = 0 
tax_salary = 0
for arg in sys.argv[1:]:
    arg_list = arg.split(':')
    try:
        idnum = int(arg_list[0])
        salary = int(arg_list[1])
    except:
        print("Parameter Error")

    tax_income = salary - salary * 0.165 - 3500

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

    tax_salary = salary - salary * 0.165 - tax_pay
    print(str(idnum) + ':' + str(format(tax_salary,".2f")))
