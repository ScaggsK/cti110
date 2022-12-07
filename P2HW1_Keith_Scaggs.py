# Travel Expense Calculator
# 4 OCT 2022
# CTI-110 P2HW1 - Travel Expense
# Keith Scaggs
#
# Get Budget, location, gas, and any other information needed from user
# Calculate expenses and remaining budget
# display location, values input and any remaining money
# all outputs need to align when ran
#
print('This program calculates and displays travel expenses', '\n')
bud = float(input('Enter Budget: '))
print()
loc =(input('Enter your travel destination: '))
print()
gas = float(input('How much do you think you will spend on gas? '))
print()
acc = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '),)
print()
print('------------TRAVEL EXPENSES-------------')
print('Location:         ', loc)
print(f'Initial Budget:    ${bud}')
print(f'Fuel:              ${gas}')
print(f'Accomodation:      ${acc}')
print(f'Food:              ${food}')
print("----------------------------------------")
print()
print(f'Remaining Balance: ${bud - (gas + acc + food)}')
