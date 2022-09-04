no_words = int(input())
no_word_list = []

word_list = [input() for e in range(no_words)]
count_words = set(word_list)

for word in count_words:
    no_word_list.append(word_list.count(word))
    
no_word_list = sorted(no_word_list, reverse=True)

# for i in no_word_list:
#     print(i, end=" ")

map(no_word_list, lambda x: print(x))