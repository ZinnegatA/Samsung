import json


data = """{ 
    "Admin": "qwerty159", 
    "Seller": "seller1337", 
    "Buyer": "guest00"  
    }"""

passwords = json.loads(data)


class Shop:
    products = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'"{self.name}"'


class Admin:
    def __init__(self, nickname):
        self.nickname = nickname
        try:
            if passwords[login] == password and login == 'Admin':
                self.login = login
                self.password = password
                print(f'Добро пожаловать, {self.nickname}! Доступ разрешен!')
            else:
                print('Неверный пароль, доступ запрещен')
        except KeyError:
            print('Пользователя с таким логином не существует, попробуйте ещё раз')

    def add_products(self, shop, *products):
        shop.products.extend(products)
        print(f'Продукты добавлены в магазин {shop}')

    def del_product(self, shop, product):
        if product in shop.products:
            shop.products.remove(product)
            print(f'{product} удален из магазина {shop}')
        else:
            print(f'Продукт {product} отсутствует в данном магазине, удаление невозможно')

    def change_characts(self, product, name, price):
        product.name = name
        product.price = price
        print(f'Характеристики успешно изменены, новое наименование продукта - {name}, новая цена - {price}')


class Seller:
    def __init__(self, nickname):
        self.nickname = nickname
        try:
            if passwords[login] == password and login == 'Seller':
                self.login = login
                self.password = password
                print(f'Добро пожаловать, {self.nickname}! Доступ разрешен!')
            else:
                print('Неверный пароль, доступ запрещен')
        except KeyError:
            print('Пользователя с таким логином не существует, попробуйте ещё раз')

    def add_products(self, shop, *products):
        shop.products.extend(products)
        print(f'Продукты добавлены в магазин {shop}')

    def del_product(self, shop, product):
        if product in shop.products:
            shop.products.remove(product)
            print(f'{product} удален из магазина {shop}')
        else:
            print(f'Продукт {product} отсутствует в данном магазине, удаление невозможно')


class Cart:
    items = []
    total_amount = 0


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Продукт "{self.name}": цена - "{self.price}"'


class Electroproducts(Product):
    def __init__(self, name, price):
        super().__init__(name, price)


class Things(Product):
    def __init__(self, name, price):
        super().__init__(name, price)


class Toys(Product):
    def __init__(self, name, price):
        super().__init__(name, price)


class Buyer:
    def __init__(self, name, wallet):
        self.name = name
        self.__wallet = wallet
        self.cart = Cart()
        try:
            if passwords[login] == password and login == 'Buyer':
                self.login = login
                self.password = password
                print(f'Добро пожаловать, {self.name}! Доступ разрешен!')
            else:
                print('Неверный пароль, доступ запрещен')
        except KeyError:
            print('Пользователя с таким логином не существует, попробуйте ещё раз')

    def buy_product(self, product):
        Cart.items.append(product)
        Cart.total_amount += product.price
        self.__wallet -= product.price
        Shop.products.remove(product)
        print(f'''В кошельке осталось {self.__wallet} средств
В корзине на данный момент товаров на {Cart.total_amount}''')

    def add_funds(self, amount):
        self.__wallet += amount
        print(f'Ваш кошелек успешно пополнен на {amount}')

    def cancel_buying(self, product):
        Cart.items.remove(product)
        Cart.total_amount -= product.price
        self.__wallet += product.price
        Shop.products.append(product)
        print(f'''В кошельке вернулось {product.price} средств, осталось {self.__wallet} денег
В корзине на данный момент товаров на {Cart.total_amount}''')

    def order(self):
        if len(self.cart.items) > 0 and self.__wallet >= 0:
            print(
                f'Ваш заказ успешно оформлен! Куплено {len(self.cart.items)} товаров на сумму {self.cart.total_amount}')
        elif len(self.cart.items) < 1:
            print('Вы не добавили ничего в корзину! Невозможно оформить заказ')
        elif self.__wallet < 0:
            print(
                'Невозможно оформить заказ! Недостаточно средств на счету! Пополните счет для продолжения оформления заказа')

    def __str__(self):
        return f'Имя покупателя: {self.name}, средств на кошельке: {self.__wallet}'


while True:
    login = input('Добро пожаловать в интернет-магазин! Пожалуйста, введите Ваш логин для идентификации: ').title()
    password = input('Введите пароль: ')
    new_user = Admin('Zinnegata')

