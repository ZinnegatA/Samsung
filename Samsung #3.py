# import random
#
# secretValue = random.randint(1, 100)
# count = 1
# while count <= 8:
#     myValue = int(input(f'Введите ваше число: , попытка номер {count}'))
#     if myValue > secretValue:
#         print('Ваше число больше загаданного')
#     elif myValue < secretValue:
#         print('Ваше число меньше загаданного')
#     else:
#         print(f'Вы победили с попытки номер {count}')
#         break
#     count += 1

# a, b = int(input()), int(input())
# sum = 0
# for i in range(b):
#     sum += a
# print(sum)

# n = int(input())
#
# for i in range(1, n + 1):
#     print(f'{i} - {i ** 2}')

# maximum = int(input())
#
# while True:
#     num = int(input())
#     if maximum < num:
#         maximum = num
#     if num == 0:
#         break
# print(maximum)

# n = int(input('Insert n: '))
# sum = 0
# for i in range(1, n * 2, 2):
#     print(i)
#     sum += i
# print(sum)

# a, b = int(input()), int(input())
# for i in range(b + 1):
#     print(i, a ** i)

# n = int(input())
# sum = 1
# for i in range(1, n + 1):
#     sum *= i
# print(sum)

# for i in range (5):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# count = 0
# for i in range(4):
#     for j in range(i + 1):
#         count += 1
#         print(count, end=' ')
#     print()

# n = int(input("количество строк: "))
# for i in range(n+1):
#     print((n-i)*" ", i*"*")

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()

