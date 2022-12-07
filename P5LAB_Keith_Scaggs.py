def days_in_feb(input_year):
    if (input_year % 4 == 0):
        if (input_year % 100 == 0):
            if (input_year % 400 == 0):
                days = 29
            else:
                days = 28
        else:
            days = 29    
    else:
        days = 28
    
    return days


if __name__ == '__main__':
    input_year = int(input())
    days = days_in_feb(input_year)
    if days == 28:
        print(input_year, "has 28 days in February.")
    else:
        print(input_year, "has 29 days in February.")