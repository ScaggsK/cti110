# CTI-110
# P4HW2 - Salary Calculator
# Keith Scaggs 
# 2022 11 15

# Code should display Employees name, hours, rate, overtime, hourly rate, and gross pay
# Allow for multiple employee inputs
# Calculate total employees, overtime paid, regual paid and total gross paid

over_hours = 0
ot_pay = 0
emp_count = 0
total_ot = 0
total_rh = 0
total_gross = 0

emp_name = input("Enter Employee's name or "'"None" to terminate: ')

while emp_name != 'None':
    hours = float(input("Enter number of hours did work " + emp_name + ' work: '))
    pay_rate = float(input("What is " + emp_name + "'s payrate: "))
    emp_count += 1
    if (hours <=40):
        over_hours = 0
        ot_pay = 0
        rh_pay = 0
        gross_pay = 0
    else:
        over_hours = (hours - 40)
        ot_pay = ((pay_rate * 1.5) * over_hours)
    rh_pay = ((hours - over_hours) * pay_rate)
    gross_pay = (rh_pay + ot_pay)
    total_ot = (total_ot + ot_pay)
    total_rh = (total_rh + rh_pay)
    total_gross = (total_gross + gross_pay)
    print('--------------------------------')
    print(emp_name)
    print()
    print(f' Hours Worked     Pay Rate     Overtime     Overtime Pay     RegHour Pay     Gross Pay')
    print('-----------------------------------------------------------------------------------------')
    print(f' {hours:<17}{pay_rate:<13}{over_hours:<13}${ot_pay:<16.2f}${rh_pay:<15.2f}${gross_pay:.2f}')
    emp_name = input("Enter Employee's name or "'"None" to terminate: ')

print()
print('Total number of employees enetered: ', emp_count)
print(f'Total amount payed for overtime: {total_ot:.2f}')
print(f'Total amount payed for regular hours: {total_rh:.2f}')
print(f'Total payed in gross: {total_gross:.2f}')
