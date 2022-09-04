string_list = list(input())
output_list = []
string_list.append("")
element = string_list[0]
element_count = 0
print
for e in string_list:
    if e != element:
        output_list.append((element_count, element))
        element = e
        element_count = 1
        continue

    element_count += 1

for e_list in output_list:
    print(e_list, end=" ")