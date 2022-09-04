array_len = input()
arr = set(input().split(" "))
A = set(input().split(" "))
B = set(input().split(" "))
happiness = 0

# for e in arr:
#     happiness += A.count(e)
#     happiness -= B.count(e)

print(sum([(i in A) - (i in B) for i in arr]))