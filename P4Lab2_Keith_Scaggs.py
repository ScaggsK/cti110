my_num = int(input())
my_num2 = int(input())

if my_num > my_num2:
    print("Second integer can't be less than the first.")
else:
    for x in range(my_num, my_num2 + 1, 5):
        print(x, end=' ')
    print()