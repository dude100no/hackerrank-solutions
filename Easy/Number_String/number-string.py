maximum = int(input())
number_string = 0
for i in range(1, maximum + 1):
    if i < 10:
        number_string *= 10
        number_string += i
    elif i < 100:
        number_string *= 100
        number_string += i
    elif i < 1000:
        number_string *= 1000
        number_string += i

print(number_string)
    