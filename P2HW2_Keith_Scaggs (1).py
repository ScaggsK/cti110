#List of Grades
#CTI-110
#P2HW2
#Keith Scaggs
#2022 10 06

#Store grades in list to display in outputs
#Used to average grades overtime
#Show lowest and highest grade
#Show sum total of all grades
#Display average with TWO decimals

mod1 = float(input("Enter grade for Module 1: " ))
mod2 = float(input("Enter grade for Module 2: " ))
mod3 = float(input("Enter grade for Module 3: " ))
mod4 = float(input("Enter grade for Module 4: " ))
mod5 = float(input("Enter grade for Module 5: " ))
mod6 = float(input("Enter grade for Module 6: " ))
allmod = [mod1, mod2, mod3, mod4, mod5, mod6]
print()
print("-------------RESULTS-------------")
print('Lowest Grade:' , min(allmod))
print('Highest Grade:' , max(allmod))
print('Sum of Grades: ', sum(allmod))
print(f'Average: {(sum(allmod)/len(allmod)):.2f}')
print('---------------------------------')
