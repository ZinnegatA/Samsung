# count sort
# unsorted_list = [0, 1, 3, 2, 4, 5, 2, 1, 5, 4]
# count = [0] * 6
# for i in unsorted_list:
#     count[i] += 1
# for i in range(6):
#     if count[i] > 0:
#         print((str(i) + ' ') * count[i], end='')

# selection sort
# from random import randint
#
#
# unsorted_lst = [randint(-10, 10) for _ in range(10)]
# for i in range(len(unsorted_lst) - 1):
#     for j in range(i + 1, len(unsorted_lst)):
#         if unsorted_lst[i] > unsorted_lst[j]:
#             unsorted_lst[i], unsorted_lst[j] = unsorted_lst[j], unsorted_lst[i]
#
# print(unsorted_lst)
