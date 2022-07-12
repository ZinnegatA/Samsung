# 1
# from random import randint
#
#
# N = int(input())
# A = [randint(0, 99) for i in range(N)]
# count = 0
# print('Исходный массив', A)
# for i in range(len(A) - 1):
#     for j in range(len(A) - 1 - i):
#         if A[j] > A[j + 1]:
#             A[j], A[j + 1] = A[j + 1], A[j]
#             count += 1
# print(A, f'Сортировка была выполнена за {count} шагов', sep='\n')

# 2
# from random import randint
#
#
# N = int(input())
# A = [randint(0, 99) for i in range(N)]
# indexes = [i for i in range(N)]
# print(indexes)
# print(A)
# for i in range(N - 1):
#     for j in range(N - 1):
#         if A[indexes[j]] > A[indexes[j + 1]]:
#             indexes[j], indexes[j + 1] = indexes[j + 1], indexes[j]
# print(indexes)
# print(A)
