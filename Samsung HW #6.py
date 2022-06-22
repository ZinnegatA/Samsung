# Task1
# x = int(input('Insert number: '))
# res = {k: v for k, v in (input('Your text: ').split() for _ in range(x))}
# print(res)

# Task2
# x = int(input('Insert number: '))
# res = {k: k ** 3 for k in range(x + 1)}
# print(res)

# Task3
# pass

# Task4
# employee = {
#     'employee1': {'name': 'Sam', 'age': 35, 'salary': 400000},
#     'employee2': {'name': 'Anna', 'age': 29, 'salary': 350000},
#     'employee3': {'name': 'John', 'age': 25, 'salary': 250000}
# }
#
# employee['employee3']['salary'] = 300000
# print(employee)

# Task5
# employee = {
#     'employee1': {'name': 'Sam', 'age': 35, 'salary': 400000},
#     'employee2': {'name': 'Anna', 'age': 29, 'salary': 350000},
#     'employee3': {'name': 'John', 'age': 25, 'salary': 250000}
# }
# del employee['employee3']
# print(employee)

# Task6
# nums = [1, 2, 3, 2, 5, 4, 10, 5, 1, 3]
# res = list(set(nums))
# print(res)

# Task6*
# x = int(input())
# num_list = [input() for _ in range(x)]
# res = list(sorted(set(num_list)))
# print(res)

# Task7
# word = input('Input text: ')
# res = {'alphas': 0, 'digits': 0}
# for c in word:
#     if c.isalpha():
#         res['alphas'] += 1
#     elif c.isdigit():
#         res['digits'] += 1
# print(res)

# Task8
# s1 = {'a', 'b', 'c', 'd', 'e', 'f', 't'}
# s2 = {'b', 'c', 'e', 'z', 'x', 'a', 'y'}
# print(f'''Union: {s1 | s2}
# Intersection: {s1 & s2}
# Difference a - b: {s1 - s2}
# Difference b - a: {s2 - s1}
# ''')

# Task9
# s1 = {'f', 't', 'c', 'a', 'x', 'd', 'e', 'b', 'y', 'z'}
# s2 = {'b', 'c', 'e', 'z', 'x', 'a', 'y'}
# print('Superset' if s1.issuperset(s2) else 'Subset')
