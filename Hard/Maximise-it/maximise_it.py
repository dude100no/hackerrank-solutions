def square(num):
    return num ** 2

line1 = input().split(" ")
k = int(line1[0])
m = int(line1[1])
k_list = []
total = 0

for i in range(k):
    entry = [int(num) for num in input().split(" ")]
    total += square(max(entry[1:]))

print(total % m)