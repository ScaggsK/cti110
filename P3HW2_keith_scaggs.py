# CTI-110
# P3HW2 - Salary
# Keith Scaggs 
# 2022 10 24

# Code should display Employees name, hours, rate, overtime, hourly rate, and gross pay

ot_hours = True
over_hours = 0
ot_pay = 0
emp_name = input('Enter Employee Name: ')
hours = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))
if (hours <=40):
    ot_hours = False
else:
    ot_hours = True
    over_hours = (hours - 40)
    ot_pay = ((pay_rate * 1.5) * over_hours)
rh_pay = ((hours - over_hours) * pay_rate)
gross_pay = (rh_pay + ot_pay)
print('--------------------------------')
print(emp_name)
print()
print('Hours Worked     Pay Rate     Overtime     Overtime Pay     RegHour Pay     Gross Pay')
print('-------------------------------------------------------------------------------------')
print(f' {hours}              {pay_rate}        {over_hours}           ${ot_pay:.2f}           ${rh_pay:.2f}        ${gross_pay:.2f}')
