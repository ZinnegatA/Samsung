# new_list = [input() for i in range(int(input()))]
# print(min(new_list), max(new_list))

# n = int(input())
# l = [int(input()) for _ in range(n)]
# m = int(input())
# if m in l:
#     print('Yes', 'Index:', l.index(m))

# new_list = [int(input()) for _ in range(int(input()))]
# res = []
# for i in range(len(new_list) - 1):
#     if new_list[i] < new_list[i + 1]:
#         res.append(new_list[i])
#
# print(*res, len(res))

# new_list = [int(input()) for _ in range(int(input()))]
# res = []
# count = 0
# flag = False
# for i in range(len(new_list) - 1, -1, -1):
#     if new_list[i] == 0:
#         flag = True
#         count += 1
#     if flag is True:
#         res.append(new_list[i])
#     if count == 2:
#         break
# print(sum(res))

# new_list = [int(input()) for _ in range(int(input()))]
# print(new_list.count(max(new_list, key=lambda x: new_list.count(x))))
