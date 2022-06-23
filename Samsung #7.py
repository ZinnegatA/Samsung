# from random import randint
#
# n = int(input())
# a = [randint(0,99) for _ in range(n)]
# b = [randint(0,99) for _ in range(n)]
# print(a, b)
# a, b = b, a
# print(a, b)

# a = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
# print(a[0], a[1], a[2], sep='\n')

# m, n = int(input()), int(input())
# a = []
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(10 * i)
#     a.append(b)
#
# print(a)

# from random import randint
#
# n = int(input())
# new_lst = [[randint(0, 99) for _ in range(n)] for _ in range(2)]
# print(new_lst)
# print('Yes' if new_lst[0] == new_lst[1] else 'No')

# n = int(input())
# new_lst = [[i for i in range(n)] for _ in range(2)]
# print(new_lst)
# print('Yes' if new_lst[0] == new_lst[1] else 'No')

# Дана матрица размера M × N и целое число K (1 ≤ K ≤ N). Вывести элементы K-го столбца данной матрицы.
# m, n, k = int(input()), int(input()), int(input())
# new_lst = [[i for i in range(m)] for _ in range(n)]
# for i in new_lst:
#     print(i[k])

# Программа запрашивает два числа N и M, затем мы создаем двумерный массив и заполняем их числами.
# Программа в конце должна посчитать количество отрицательных чисел, и при выводе их заменить символом "х".
# from random import randint
# n, m = int(input()), int(input())
# new_list = [[randint(-100, 100) for _ in range(n)] for _ in range(m)]
# for i in range(len(new_list)):
#     for j in range(len(new_list[i])):
#         if new_list[i][j] < 0:
#             new_list[i][j] = 'x'
#     print(*new_list[i])

# Программа запрашивает два числа N и M, затем мы создаем двумерный массив и заполняем их
# числами. Программа должна вывести количество отрицательных чисел в каждой строке.
# from random import randint
# n, m = int(input()), int(input())
# new_list = [[randint(-100, 100) for _ in range(n)] for _ in range(m)]
# for i in new_list:
#     count = 0
#     for j in i:
#         if j < 0:
#             count += 1
#     print(*i)
#     print(count)

# Программа запрашивает число N, затем мы создаем двумерный массив N x N и заполняем их
# числами. Программа должна вывести массив таким образом, как в нижних примерах.
# from random import randint
# n = int(input())
# new_list = [[randint(0, 99) for _ in range(n)] for _ in range(n)]
# for i in range(len(new_list)):
#     for j in range(len(new_list[i])):
#         if i == j:
#             new_list[i][j] = 'x'
#     print(*new_list[i])

# n = int(input())
# matrix = [[1] * n for _ in range(n)]
#
# for i in range(n):
#     matrix[i][n - 1 - i] = 0
#     for j in range(n):
#         if i > n - 1 - j:
#             matrix[i][j] = 2
#         print(matrix[i][j], end=" ")
#     print()
