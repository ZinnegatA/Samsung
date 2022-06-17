# Task1
# login, password = input(), input()
# if login == 'admin' and password == 'my_super_secure_password':
#     print('Welcome, admin!')
# else:
#     print("Don't try, bad guy!")

# Task2
# a, b = int(input()), int(input())
# print('1' if a > b else '-1')

# Task3
# num = int(input())
# if num % 4 != 0:
#     print('NO')
# elif num % 100 == 0:
#     if num % 400 == 0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('YES')

# Task4
# print('Even' if int(input()) % 2 == 0 else 'Odd')

# Task5
# kzt = int(input('Введите сумму в тенге: '))
# eur = 522.38
# dol = 428.38
# rub = 5.82
# res = int(input('''На какую валюту Вы хотите обменять свои тенге:
# 1) Евро
# 2) Доллары
# 3) Рубли
# '''))
# if res == 1:
#     print(f'Вам будет выдано {round(kzt / eur, 2)} евро')
# elif res == 2:
#     print(f'Вам будет выдано {round(kzt / dol, 2)} долларов')
# elif res == 3:
#     print(f'Вам будет выдано {round(kzt / rub, 2)} рублей')

# Task6
# n = int(input())
# for i in range(n + 1):
#     print(i ** 2, end=' ')

# Task7
# num = input()
# amount = 0
# for c in num:
#     amount += int(c)
# print(amount)

# Task8
# num = input()
# amount = 0
# for c in num:
#     amount += int(c)
# print(round(amount / len(num), 2))

# Task9
# word = input()
# print('You catch a palindrome' if word == word[::-1] else 'Not palindrome')
