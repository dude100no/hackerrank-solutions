num = int(input())

unique_words = []
all_words = []
output = []

for i in range(num):
    word = input()
    all_words.append(word)
    if word not in unique_words:
        unique_words.append(word)
        
for i in range(len(unique_words)):
    output.append(str(all_words.count(unique_words[i])))

print(len(unique_words))
print(" ".join(output))