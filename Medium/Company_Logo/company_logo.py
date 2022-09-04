logo = input("- ")
unique_char = set(logo)
charqty_list = []
output = []

for c in unique_char:
    charqty_list.append([c, logo.count(c)])

list_sorted = False
number_sorted = False
while not list_sorted:
    if not number_sorted:
        number_sorted = True
        list_sorted = False
        for i in range(len(charqty_list)):
            if i != len(charqty_list) - 1:
                if charqty_list[i][1] < charqty_list[i + 1][1]:
                    charqty_list[i], charqty_list[i + 1] = charqty_list[i + 1], charqty_list[i]
                    number_sorted = False
    
    else:
        list_sorted = True
        for i in range(len(charqty_list)):
            if i != len(charqty_list) - 1:
                matching_num = charqty_list[i][1]
                if matching_num == charqty_list[i + 1][1]:
                    if ord(charqty_list[i][0]) > ord(charqty_list[i + 1][0]):
                        charqty_list[i], charqty_list[i + 1] = charqty_list[i + 1], charqty_list[i]
                        list_sorted = False

for i in range(len(charqty_list)):
    if i < 3:
        print(charqty_list[i][0], charqty_list[i][1], sep=" ")
        continue
    break