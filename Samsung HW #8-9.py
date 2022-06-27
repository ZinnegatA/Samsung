# Task1
# def greeting():
#     return 'Hello'
#
#
# print(greeting())

# Task2
# def greeting(username):
#     return f'Hello, {username}!'
#
#
# print(greeting(input()))

# Task3
# def greeting(username='anonym'):
#     return f'Hello, {username}!'
#
#
# print(greeting())

# Task4
# def maximum_number(x, y):
#     return max(x, y)
#
#
# print(maximum_number(int(input()), int(input())))

# Task5
# def min_element(numbers):
#     return min(numbers)
#
#
# print(min_element([i for i in range(5)]))

# Task6
# def extremus(numbers):
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return minimum, maximum
#
#
# min_num, max_num = extremus([0, -5, 12, 36, -12])
# print(min_num, max_num)

# Task7
# def average(*args):
#     return int(sum(args) / len(args))
#
#
# answer = average(5, 12, 3, 4)
# print(answer)

# Task8
# def dictionary_printer(**kwargs):
#     for k, v in kwargs.items():
#         print(f'Key: {k}, Value: {v}')
#
#
# dictionary_printer(id=1, name='Python', count=5)

# Task9*
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
#
#
# print(factorial(int(input())))
