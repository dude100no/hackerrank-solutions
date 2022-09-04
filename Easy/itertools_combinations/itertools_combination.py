from itertools import combinations

# word_entry = input().split(" ")
word_entry = "HACK 2".split(" ")
word_list = []
new_word_list = []
print(word_entry[0])
word_ord = [ord(e) for e in word_entry[0]]
word_ord.sort()
print(word_ord)
for i in range(1, int(word_entry[1]) + 1):
    print(i)
    word_list += list(combinations(word_ord, i))

print(word_list)

for chunk_i in range(len(word_list)):
    new_word_list.append([])
    for letter_i in range(len(word_list[chunk_i])):
        new_word_list[chunk_i].append(chr(word_list[chunk_i][letter_i]))
    print("".join(new_word_list[chunk_i]))