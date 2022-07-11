# Task1
# try:
#     with open('myfile', 'r') as f:
#         print(f.read())
# except FileNotFoundError:
#     print(f'Такого файла не найдено')

# Task2
# try:
#     with open('mynewfile', 'r', encoding='utf-8') as f:
#         f.write('Привет')
# except Exception:
#     print('Запись в этот файл невозможна, файл открыт в режиме чтения')
# except BaseException:
#     print('Запись в этот файл невозможна, файл открыт в режиме чтения')

# Task3
# f = open('task10-3', 'r')
# try:
#     f.write('is it right?')
# except Exception as e:
#     print(e)
# else:
#     print('Вы записали в файл Вашу строку')
# finally:
#     f.close()

# Task4
# class CriticalMassException(Exception):
#     def __init__(self, critical_mass):
#         self.critical_mass = critical_mass
#         self.message = f'Critical mass is more than 2 kg - {self.critical_mass}'
#
#     def __str__(self):
#         return self.message
#
#
# def reactor_on(m, c):
#     try:
#         if m > 2:
#             raise CriticalMassException(m)
#         print(m * c ** 2)
#         return m * c ** 2
#     except CriticalMassException as e:
#         print(e)
#         return e
#
#
# reactor_on(1, 2)

# Task5
# class PermissionDenied(Exception):
#     def __init__(self, username, action):
#         self.username = username
#         self.action = action
#
#     def __str__(self):
#         return f'User {self.username} denied access to {self.action}'
#
#
# database = {
#     'admin': {'actions': ["all"]},
#     'user1': {'actions': ["read file"]},
#     'user2': {'actions': ["write file", "read file"]},
#     'user3': {'actions': []}
# }
#
# user, act = input(), input()
# try:
#     if act in database[user]['actions'] or 'all' in database[user]['actions']:
#         print('Действие выполнено')
#     else:
#         print('У Вас нет доступа к этому действию')
# except KeyError:
#     raise PermissionDenied(user, act)
