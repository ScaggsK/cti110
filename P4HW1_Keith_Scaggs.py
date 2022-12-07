#Score list
#CTI-110
#P4HW1
#Keith Scaggs
#2022 11 10

#ask how many grades to enter
#scores should be between 0-100
#no grades lower than 0 or more than 100
#Store grades in list to display in outputs
#Used to average grades overtime
#Show lowest
#drop lowest grade
#list of grades
#Show letter grade
#Display average with TWO decimals

scores = []

num_scores = int(input('How many scores do you want to enter? '))
print()

for x in range(num_scores):
    score = float(input('Enter score #' + str(x+1) +': '))
    while score <0 or  score >100:
        print("INVALID score entered")
        print('Score should be between 0 and 100')
        score = float(input('Enter score #' + str(x+1) +' again: '))
    scores.append(score)
print()
print("-------------RESULTS-------------")
print('Lowest Grade :' , min(scores))
scores.remove(min(scores))
print('Modified List:' , scores)
avg = (sum(scores)/len(scores))
print(f'Average      : {avg:.2f}')
if avg >= 90:
    print('Grade        : A')
elif avg >= 80:
    print('Grade        : B')
elif avg >= 70:
    print('Grade        : C')
elif avg >= 60:
    print('Grade        : D')
else:
    print('Grade        : F')
print('---------------------------------')
