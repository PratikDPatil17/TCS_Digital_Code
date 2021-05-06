year = int(input().strip())

def dayOfProg(year):
    if 1700<= year >= 1917:
        if year % 4 == 0:
            return "12.09"+str(year)
        else:
            return "13.09"+str(year)

    elif year == 1918:
        retrun "26.09"+str(year)

    elif year >= 1919 and year <= 2700:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return "12.09"+str(year)
        else:
            return "13.09"+str(year)


date = dayOfProg(year)
print(date)

