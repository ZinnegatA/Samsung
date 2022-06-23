# Task1
# from random import randint
# n, m = int(input()), int(input())
# new_lst = [[randint(0, 99) for _ in range(n)] for _ in range(m)]
# for i in new_lst:
#     print(*i)
#     print(max(i))

# Task2
# from random import randint
# n = int(input())
# new_lst = [[randint(0, 99) for _ in range(n)] for _ in range(n)]
# for i in new_lst:
#     for j in i:
#         print(str(j).rjust(2, '0'), end=' ')
#     print()
# new_lst.reverse()
# print('__________')
# for i in new_lst:
#     for j in i:
#         print(str(j).rjust(2, '0'), end=' ')
#     print()

# Task3
# from random import randint
# n, m = int(input()), int(input())
# new_lst = [[randint(0, 99) for _ in range(n)] for _ in range(m)]
# for i in new_lst:
#     for j in i:
#         print(str(j).rjust(2, '0'), end=' ')
#     print()
#
# for i in range(1, len(new_lst), 2):
#     map(int, new_lst[i])
#     print(f'Average number for new_list[{i}]: {sum(new_lst[i]) / len(new_lst[i])}')
