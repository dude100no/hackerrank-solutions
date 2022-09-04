string = input("Enter string: ").upper()
# string = "BANANA"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"

stuart_pt = 0
kevin_pt = 0

for i in range(len(string)):
    if string[i] in consonants:
        stuart_pt += len(string) - i
    elif string[i] in vowels:
        kevin_pt += len(string) - i

if stuart_pt > kevin_pt:
    print("Stuart {}".format(stuart_pt))
elif kevin_pt > stuart_pt:
    print("Kevin {}".format(kevin_pt))
else: print("Draw")