string = input("Enter string: ")
#string = "AABCAAADA"
k = int(input("Enter a factor: "))

string_list = []
output_list = []

for i in range(0, len(string), k):
    string_list.append(string[i:i+k])

for substring in string_list:
    present = []
    output_substring = ""
    for letter in substring:
        if letter not in present:
            output_substring += letter
            present.append(letter)

    output_list.append(output_substring)

for substring in output_list:
    print(substring)