# def maximum_num(a, b, c):
#     return max(a, b, c)
#
#
# print(maximum_num(1, 2, 3))

# def massive_reversed(massive):
#     massive.reverse()
#     return massive
#
#
# print(massive_reversed([[1, 2, 3], [2, 3, 4], [5, 6, 7]]))

# def massive_func(massive):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     res = []
#     for word in massive:
#         count = 0
#         for c in word:
#             if c in vowels:
#                 count += 1
#         if count >= 4:
#             res.append(word)
#     return res
#
#
# print(massive_func(['arman', 'erbolat', 'armagedon', 'avadakedavra', 'lamusicasuena']))

# def num_massive(massive, n):
#     res = [el for el in massive if el == massive.index(el) and el % n != 0]
#     return res
#
#
# print(num_massive([5, 1, 6], 2))

# def func(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return 'FizzBuzz'
#     elif num % 3 == 0:
#         return 'Fizz'
#     elif num % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(num)
#
#
# print(func(4))

# def func(a, b, c):
#     return str(a * b)[-1] == str(c)[-1]
#
#
# print(func(12, 215, 2142))

# def func(groceries):
#     res = 0
#     for g in groceries:
#         res += g['price'] * g['quantity']
#     return res
#
#
# print(func([{'price': 500, 'quantity': 2}, {'price': 1.5, 'quantity': 3}, {'price': 200, 'quantity': 2}]))

# def func(year):
#     for y in range(year + 1, 9999):
#         res = 0
#         for num in str(y):
#             if str(y).count(num) == 1:
#                 res += 1
#         if res == 4:
#             return y
#
#
# print(func(2021))

# def func(year):
#     for y in range(year + 1, 9999):
#         if len(set(str(y))) == 4:
#             return y
#
# print(func(1990))

