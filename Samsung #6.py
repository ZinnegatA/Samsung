# a_dict = {}
# for i in range(0, 10):
#     a_dict[i] = input("Введите значение: ")
#
# print(a_dict)


# n = int(input())
# new_dict = {}
# for i in range(1, n + 1):
#     new_dict[i] = i ** 2
#
# print(new_dict)

# employee = {
#     'employee1': {'name': 'Sam', 'age': 35, 'salary': 400000},
#     'employee2': {'name': 'Anna', 'age': 29, 'salary': 350000},
#     'employee3': {'name': 'John', 'age': 25, 'salary': 250000}
# }
#
# employee['employee3']['salary'] = 300000
# print(employee)

# login, password = input(), input()
# users = {
#     "user": "qwerty", "user2": "qwerty2", "user3": "qwerty3"
# }
# print("Authentication completed" if users[login] == password else "Incorrect login or password")

# dict1 = {1: [10, 2, 3, 2, 4, 5, 6, 8]}
# res = set(dict1[1])
# print(res)

# items = {
#     6: 'палатка',
#     4: 'удочка',
#     2: 'салфетки',
#     5: 'спальный мешок',
#     3: 'термос',
#     1: 'жвачка',
# }
# n = int(input('KG: '))
# count = 0
# stuff = []
#
# while n != count:
#     a = int(input('Insert number of item: '))
#     count += a
#     stuff.append(items[a])
#
# print(stuff)

# stuff = {'палатка': 5, "термос": 2, "удочка": 3, "салфетки": 4, "жвачка": 1, "спальный мешок": 6}
# limit = int(input())
# backpack = 0
# res = []
# while limit >= backpack:
#     for k, v in stuff.items():
#         backpack += v
#         res.append(k)

stuff = {'палатка': 5, "термос": 2, "удочка": 3, "салфетки": 4, "жвачка": 1, "спальный мешок": 6}
limit = int(input())
backpack = 0
res = []
for k, v in stuff.items():
    while limit > backpack:
        if backpack + v > limit:
            break
        backpack += v
        res.append(k)
        break
print(res)

