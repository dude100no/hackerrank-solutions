def Leap_Year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        if year % 400 == 0:
            return True

    return False

year = int(input("-"))
print(Leap_Year(year))