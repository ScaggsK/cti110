# Travel Expense Calculator
# 20 Sept 2022
# CTI-110 P1HW2 - Travel Expense
# Keith Scaggs
#
# Get Budget, location, gas, and any other information needed from user
# Calculate budget and remaining budget
# display location, values input and any remaining money
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
print('Location: ',loc)
print('Initial Budget: ', bud)
print()
print('Fuel: ', gas)
print('Accomodation: ', acc)
print('Food: ', food)
print()
print('Remaining Balance: ', bud - (gas + acc + food))
