# a quick math quiz
# 29 Nov 2022
# CTI-110 P5HW2 - Math Quiz
# Keith Scaggs
# program should have 3 options to choose from, 1 add, 2 subtract, and 3 exit
# if to high tell the user its too high
# if too low tell the user its too low
# when correct congrdulate the user and take back to menu

import random

def main():
    print('Welcome to Math Quiz\n')
    while True:
        print('MAIN MENU')
        print('-------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addProblem()
        elif choice == '2':
            subProblem()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break

def addProblem():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    print(f' {num1}')
    print(f'+{num2}')
    print('Enter answer.')
    ans = int(input())
    while ans!=(num1 + num2):
        if ans<(num1 + num2):
            print('Sorry, guess is too low.')
        else: print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('Congratulations!!!! Your answer is correct...\n')

def subProblem():
    num_1 = random.randint(10, 99)
    num_2 = random.randint(10, 99)
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    print(f' {num_1}')
    print(f'-{num_2}')
    print('Enter answer.')
    ans = int(input())
    while ans != (num_1 - num_2):
        if ans < (num_1 - num_2):
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('Congratulations!!!! Your answer is correct...\n')

main()
