# Фибоначчи

# def fib(a):
#     if a == 1:
#         return 0
#     elif a == 2:
#         return 1
#     return fib(a - 1) + fib(a - 2)
#
# for i in range(1, 15):
#

# def san(n):
#     if n > 1:
#         san(n - 1)
#     print(n)
#
#
# san(6)

# def func(n):
#     if n != 0:
#         return n % 10 + func(n // 10)
#     else:
#         return n
#
#
# print(func(179))

# from functools import reduce
#
# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# pos, neg = len(list(filter(lambda x: x > 0, new_list))), reduce(lambda x, y: x + y,
#                                                                 filter(lambda x: x < 0, new_list))
# print(pos, neg)

# def func(word):
#     if '-' in word:
#         return word.split('-')[0] + ''.join(map(lambda x: x[0].upper() + x[1:], word.split('-')[1:]))
#     elif '_' in word:
#         return ''.join(map(lambda x: x[0].upper() + x[1:], word.split('_')))
#
#
# print(func(input()))
