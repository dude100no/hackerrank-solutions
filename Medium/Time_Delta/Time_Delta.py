# t1 = input()
# t2 = input()
t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"

t1 = t1.split(" ")
t2 = t2.split(" ")

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# [day, month, year, hour, min, sec, time_diff]
t1_list = []
t2_list = []

for i in range(1, len(t1)):
    if i == 2:
        t1_list.append(month.index(t1[i]))
        continue
    
    if i == 4:
        t1_list.append(int(t1[i][:2]))
        t1_list.append(int(t1[i][3:5]))
        t1_list.append(int(t1[i][6:]))
        continue

    if i == 5:
        t1_list.append(t1[i][0])
        t1_list.append(int(t1[i][1:3]))
        t1_list.append(int(t1[i][3:]))
        continue

    t1_list.append(int(t1[i]))

for i in range(1, len(t2)):
    if i == 2:
        t2_list.append(month.index(t2[i]))
        continue
    
    if i == 4:
        t2_list.append(int(t2[i][:2]))
        t2_list.append(int(t2[i][3:5]))
        t2_list.append(int(t2[i][6:]))
        continue

    if i == 5:
        t2_list.append(t2[i][0])
        t2_list.append(int(t2[i][1:3]))
        t2_list.append(int(t2[i][3:]))
        continue

    t2_list.append(int(t2[i]))

print(t1_list, "\n", t2_list)


#t1 convert to UTF time
if t1_list[-3] == "-":
    t1_list[4] += t1_list[-1]
    t1_list[3] += t1_list[-2]
    if t1_list[4] > 60:
        if t1_list[3] > 24:
            if t1_list[0] >
elif t1_list[-3] == "+":
    t1_list[4] -= t1_list[-1]
    t1_list[3] -= t1_list[-2]