# class CPU:
#     def __init__(self, cash_memory, price, weight):
#         self.cash_memory = cash_memory
#         self.price = price
#         self.weight = weight
#
#
# class HDD:
#     def __init__(self, memory, price, weight):
#         self.memory = memory
#         self.price = price
#         self.weight = weight
#
#
# class Laptop:
#     def __init__(self, name, price, weight, hdd, cpu):
#         self.name = name
#         self.price = price
#         self.weight = weight
#         self.hdd = hdd
#         self.cpu = cpu
#
#     def get_total_price(self):
#         return self.price + self.hdd.price + sum([el.price for el in self.cpu])
#
#     def get_total_cpu_memory(self):
#         return sum([el.cash_memory for el in self.cpu])
#
#     def get_total_weight(self):
#         return self.weight + self.hdd.weight + sum([el.weight for el in self.cpu])
#
#
# intel = CPU(96, 200, 1)
# amd = CPU(192, 300, 2)
#
# seagate = HDD(2000, 150, 2)
# kingston = HDD(1000, 100, 1)
#
# samsung = Laptop('Samsung', 1500, 2, seagate, [intel, amd])
# acer = Laptop('Acer', 1200, 3, kingston, [intel, amd])
# asus = Laptop('Asus', 1800, 2, seagate, [intel, amd, intel, amd])
# digma = Laptop('Digma', 800, 5, kingston, [intel, amd, intel, amd])
# lg = Laptop('LG', 500, 1, seagate, [intel, amd, intel, amd, intel, amd, intel, amd])
# flatron = Laptop('Flatron', 1100, 6, kingston, [intel, amd, intel, amd, intel, amd, intel, amd])


# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class User:
#     id = Descriptor()
#     login = Descriptor()
#     password = Descriptor()
#     role = Descriptor()
#
#     def __init__(self, id, login, password, role):
#         self.id = id
#         self.login = login
#         self.password = password
#         self.role = role
#
#     def get_all_data(self):
#         return [el for el in self.__dict__.values()]
#
#
# me = User(15, 'Руслан', 123456, "user")
# admin = User(16, "Адильбек", 654321, "admin")
# engineer = User(20, "Дмитрий", 145236, "engineer")
# user4 = User(1, 'User4', 123456, "user")
# user5 = User(2, 'User5', 124536, "user")
# user6 = User(3, 'User6', 321456, "user")
# user7 = User(4, 'User7', 124356, "user")
# user8 = User(5, 'User8', 123654, "user")
# user9 = User(6, 'User9', 123645, "user")
# user10 = User(7, 'User10', 321465, "user")
#
# users = [me, admin, engineer, user4, user5, user6, user7, user8, user9, user10]
# for user in users:
#     print(user.password)

# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class Book:
#     name = Descriptor()
#     author = Descriptor()
#     isbn = Descriptor()
#     price = Descriptor()
#
#     def __init__(self, name, author, isbn, price):
#         self.name = name
#         self.author = author
#         self.isbn = isbn
#         self.price = price
#
#     def get_all_data(self):
#         return [el for el in self.__dict__.values()]
#
#
# class Library:
#     name = Descriptor()
#     city = Descriptor()
#     books = Descriptor()
#
#     def __init__(self, name, city, books):
#         self.name = name
#         self.city = city
#         self.books = books
#         self.__size_of_books = 0
#
#     def size(self):
#         return self.__size_of_books
#
#     def price_sum(self):
#         return sum(book.price for book in self.books)
#
#     def get_book(self, index):
#         return self.books[index]
#
#     def add_book(self, book):
#         self.books.append(book)
#         self.__size_of_books += 1
#
#
# book1 = Book("Книга 1", "Пушкин", 147258, 1000)
# book2 = Book("Книга 2", "Толстой", 145236, 1200)
# book3 = Book("Книга 3", "Лермонтов", 147852369, 1500)
# book4 = Book("Книга 4", "Маяковский", 159462, 900)
# book5 = Book("Книга 5", "Перро", 789456123, 1300)
# book6 = Book("Книга 6", "Гоголь", 112345, 2000)
# book7 = Book("Книга 7", "Крылов", 15241654, 1800)
# book8 = Book("Книга 8", "Тургенев", 123456974, 3000)
# book9 = Book("Книга 9", "Высоцкий", 15645964, 1100)
# book10 = Book("Книга 10", "Риордан", 1593232, 1700)
#
# lib1 = Library('Библиотека Алматы', 'Алматы', [])
# lib2 = Library('Библиотека Шымкента', 'Шымкент', [])
#
# lib1.add_book(book1)
# lib1.add_book(book2)
# lib1.add_book(book3)
# lib1.add_book(book4)
# lib2.add_book(book5)
# lib2.add_book(book6)
# lib2.add_book(book7)
# lib2.add_book(book8)
# lib2.add_book(book9)
# lib2.add_book(book10)
#
# print(lib1.size(), [book.price for book in lib1.books], lib1.price_sum())
# print(lib2.size(), [book.price for book in lib2.books], lib2.price_sum())
