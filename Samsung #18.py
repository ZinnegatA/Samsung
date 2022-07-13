from random import randint
import datetime

# 1 Bubble Sort
# unsorted_list = [randint(-10, 10) for _ in range(100)]
# print(f'Исходный массив: {unsorted_list}')
# start = datetime.datetime.today()
# for i in range(len(unsorted_list) - 1):
#     for j in range(len(unsorted_list) - 1 - i):
#         if unsorted_list[j] > unsorted_list[j + 1]:
#             unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
# finish = datetime.datetime.today()
# print(f'Отсортированный массив: {unsorted_list}', f'Сортировка была выполнена за {finish - start} времени', sep='\n')


# 2 Merge Sort
# unsorted_list = [randint(-10, 10) for _ in range(100)]
# print(f'Исходный массив: {unsorted_list}')
# start = datetime.datetime.today()
#
#
# def merge_lists(list1, list2):
#     res = []
#     i = j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             res.append(list1[i])
#             i += 1
#         else:
#             res.append(list2[j])
#             j += 1
#
#     if i < len(list1):
#         res += list1[i:]
#     if j < len(list2):
#         res += list2[j:]
#     return res
#
#
# def merge_sort(my_list):
#     if len(my_list) == 1:
#         return my_list
#     middle = len(my_list) // 2
#     left = merge_sort(my_list[:middle])
#     right = merge_sort(my_list[middle:])
#     return merge_lists(left, right)
#
#
# print(f'Отсортированный массив: {merge_sort(unsorted_list)}')
# finish = datetime.datetime.today()
# print(f'Сортировка была выполнена за {finish - start} времени')
