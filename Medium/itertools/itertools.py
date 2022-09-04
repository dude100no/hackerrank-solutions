from itertools import combinations

str_len = int(input())
str_input = input().split(" ")
str_choose_count = int(input())

str_combi = list(combinations(str_input, str_choose_count))
num_combi = len(str_combi)

list_of_a = list(filter(lambda li: True if "a" in li else False, str_combi))
num_of_a = len(list_of_a)

print(round(num_of_a / num_combi, 3))