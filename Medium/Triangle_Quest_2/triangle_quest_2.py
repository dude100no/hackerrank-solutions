for i in range(1, int(input()) + 1):
    print(((10**i - 1)//9)**2)
    print(10 ** (i * 2 - 2) + sum([(num_f * (10 ** (i * 2 - num_f - 1))) for num_f in range(2, i + 1)]) + sum([(num_b * (10 ** (num_b - 1))) for num_b in range(1, i)]))