string = input("Enter string: ").upper()
# string = "BANANA"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"

conInS = []
vowInS = []

# stuart_words = []
# kevin_words = []

stuart_pt = 0
kevin_pt = 0

for con in consonants:
    if con in string:
        conInS.append(con)

for vow in vowels:
    if vow in string:
        vowInS.append(vow)

for string_i in range(len(string)):
    for string_i_add in range(1, len(string) - string_i + 1):
        word = string[string_i:string_i + string_i_add]
        if word[0] in conInS:
            # stuart_words.append(word)
            stuart_pt += 1
        elif word[0] in vowInS:
            # kevin_words.append(word)
            kevin_pt += 1

# print(stuart_words)
# print(kevin_words)

# if len(stuart_words) > len(kevin_words):
#     print("Stuart {}".format(len(stuart_words)))
# elif len(stuart_words) < len(kevin_words):
#     print("Kevin {}".format(len(kevin_words)))
# else:
#     print("Draw")

if stuart_pt > kevin_pt:
    print("Stuart {}".format(stuart_pt))
elif kevin_pt > stuart_pt:
    print("Kevin {}".format(kevin_pt))
else: print("Draw")