def piling_up(list_, list_len, check = []):
    # print(list_, check)
    if len(check) == list_len:
        return "Yes"
    elif len(check) == 0:
        if list_[0] > list_[-1]:
            check.append(list_[0])
            list_.pop(0)
            return piling_up(list_, list_len, check)
        else:
            check.append(list_[-1])
            list_.pop(-1)
            return piling_up(list_, list_len, check)
    elif len(check) > 0:
        if list_[0] > int(check[-1]) or list_[-1] > int(check[-1]):
            return "No"
        elif list_[0] > list_[-1]:
            check.append(list_[0])
            list_.pop(0)
            return piling_up(list_, list_len, check)
        else:
            check.append(list_[-1])
            list_.pop(-1)
            return piling_up(list_, list_len, check)

    

t = int(input())
cube_list = []

for test_case in range(t):
    no_of_cubes = int(input())
    cubes = list(map(lambda x: int(x), input().split(" ")))
    cube_list.append(cubes)

# print(cube_list)

for test_case in range(t):
    case = cube_list[test_case]
    print(piling_up(case, len(case), []))