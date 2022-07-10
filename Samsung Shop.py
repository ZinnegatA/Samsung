import json

data = """{ 
    "Admin": "qwerty159", 
    "Seller": "seller1337", 
    "Buyer": "guest00"  
    }"""

passwords = json.loads(data)

login = input('Добро пожаловать в интернет-магазин! Пожалуйста, введите Ваш логин для идентификации: ').title()
password = input('Введите пароль: ')


class Shop:
    products = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'"{self.name}"'


class Admin:
    def __init__(self, nickname):
        self.nickname = nickname
        if passwords[login] == password:
            self.login = login
            self.password = password
            print(f'''Добро пожаловать, {self.nickname}! Доступ разрешен!
У Вас есть доступ к добавлению, удалению и редактированию товаров в магазинах, для этого введите одну из следующих цифр:
1) Добавить новый магазин в программу
2) Добавить товар в магазин
3) Удалить товар из магазина
4) Редактировать товар в магазине
Для выхода из программмы введите нажмите кнопку 0''')
        else:
            print('Неправильный логин или пароль, доступ запрещен')
            exit()

    def add_products(self, shop, *products):
        shop.products.extend(products)
        print(f'Продукты добавлены в магазин {shop}')

    def del_product(self, shop, product):
        if product in shop.products:
            shop.products.remove(product)
            print(f'{product} удален из магазина {shop}')
        else:
            print(f'"{product}" отсутствует в данном магазине, удаление невозможно')

    def change_characts(self, product, name, price):
        product.name = name
        product.price = price
        print(f'Характеристики успешно изменены, новое наименование продукта - {name}, новая цена - {price}')

    def create_shop(self, name):
        return Shop(name)


class Seller:
    def __init__(self, nickname):
        self.nickname = nickname
        if passwords[login] == password and login == 'Seller':
            self.login = login
            self.password = password
            print(f'''Добро пожаловать, {self.nickname}! Доступ разрешен!
У Вас есть доступ к добавлению и удалению товаров в магазинах, для этого введите одну из следующих цифр:
1) Добавить товар в магазин
2) Удалить товар из магазина
Для выхода из программмы введите нажмите кнопку 0''')
        else:
            print('Неправильный логин или пароль, доступ запрещен')
            exit()

    def add_products(self, shop, *products):
        shop.products.extend(products)
        print(f'Продукты добавлены в магазин {shop}')

    def del_product(self, shop, product):
        if product in shop.products:
            shop.products.remove(product)
            print(f'{product} удален из магазина {shop}')
        else:
            print(f'"{product}" отсутствует в данном магазине, удаление невозможно')


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
        if passwords[login] == password and login == 'Buyer':
            self.login = login
            self.password = password
            print(f'''Добро пожаловать, {self.name}! Доступ разрешен!
У Вас есть доступ к добавлению и удалению товара в корзине, пополнению своего кошелька, а также Вы можете оформить заказ, для этого введите одну из следующих цифр:
1) Добавить товар в корзину
2) Удалить товар из корзины
3) Пополнить кошелек
4) Оформить заказ
Для выхода из программмы введите нажмите кнопку 0''')
        else:
            print('Неправильный логин или пароль, доступ запрещен')
            exit()

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


if login == 'Admin':
    adm = Admin(input('Введите свой никнейм: '))
    while True:
        admin_button = int(input())
        if admin_button == 1:
            shop = adm.create_shop(input('Введите имя нового магазина: '))
            print(f'Магазин "{shop.name}" успешно создан!')
        elif admin_button == 2:
            try:
                product = Product(input('Наименование добавляемого товара: ').title(),
                                  int(input('Введите цену товара: ')))
                adm.add_products(shop, product)
                print(f'"{product}" успешно добавлен в магазин {shop.name}')
            except ValueError:
                print('Цена должна быть числом')
        elif admin_button == 3:
            prod = input('Введите название продукта, который требуется удалить: ')
            for product in shop.products:
                if prod.title() == product.name:
                    adm.del_product(shop, product)
        elif admin_button == 4:
            prod = input('Введите название продукта для редактирования: ').title()
            flag = False
            for product in shop.products:
                if prod.title() == product.name:
                    adm.change_characts(product,
                                        input('Введите новое наименование продукта: ').title(),
                                        int(input('Введите новую цену товара: ')))
                    flag = True
            if flag is False:
                print('Невозможно изменить характеристики несуществующего продукта, проверьте наименование')
        elif admin_button == 0:
            print(f'Завершение рабочего сеанса, до свидания, {login}')
            relog = int(input('Для входа под другим логином нажмите 1, для завершения работы программы нажмите 0: '))
            if relog == 1:
                login = input(
                    'Для смены учетной записи введите Ваш логин для идентификации: ').title()
                password = input('Введите пароль: ')
                pass
            elif relog == 0:
                exit()
        print('''Для продолжения использования программы повторно введите одну из цифр, для выхода введите 0
''')

        if login == 'Seller':
            seller = Seller(input('Введите свой никнейм: '))
            while True:
                seller_button = int(input())
                if seller_button == 1:
                    try:
                        product = Product(input('Наименование добавляемого товара: ').title(),
                                          int(input('Введите цену товара: ')))
                        seller.add_products(Shop, product)
                        print(f'"{product}" успешно добавлен в магазин {shop.name}')
                    except ValueError:
                        print('Цена должна быть числом')
                elif seller_button == 2:
                    prod = input('Введите название продукта, который требуется удалить: ')
                    for product in shop.products:
                        if prod.title() == product.name:
                            seller.del_product(shop, product)
                elif seller_button == 0:
                    print(f'Завершение рабочего сеанса, до свидания, {login}')
                    exit()
                print('''Для продолжения использования программы повторно введите одну из цифр, для выхода введите 0
''')
                if login == 'Buyer':
                    buyer = Buyer(input('Введите своё имя: '), int(input('Какую сумму Вы имеете на счету? ')))
                    while True:
                        buyer_button = int(input())
                        if buyer_button == 1:
                            prod = input('Введите название продукта для покупки: ').title()
                            flag = False
                            for product in shop.products:
                                if prod.title() == product.name:
                                    buyer.buy_product(product)
                                    flag = True
                            if flag is False:
                                print(
                                    'Такого продукта нет в наличии')
                        elif buyer_button == 2:
                            prod = input('Введите название продукта, который Вы хотите удалить из корзины: ')
                            for product in shop.products:
                                if prod.title() == product.name:
                                    buyer.cancel_buying(product)
                        elif buyer_button == 3:
                            buyer.add_funds(input('На какую сумму Вы хотите пополнить кошелек? '))
                        elif buyer_button == 4:
                            buyer.order()
                        elif buyer_button == 0:
                            print(f'Завершение рабочего сеанса, до свидания, {login}')
                            exit()
                    print('''Для продолжения использования программы повторно введите одну из цифр, для выхода введите 0
        ''')

                else:
                    print('Пользователя с таким логином не найдено в системе')

elif login == 'Seller':
    print(
        f'Уважаемый пользователь, взаимодействие с программой на данный момент невозможно, так как администратором не был создан ни один магазин. Обратитесь к администратору для создания магазина.')
elif login == 'Buyer':
    print(
        f'Уважаемый пользователь, взаимодействие с программой на данный момент невозможно, так как администратором не был создан ни один магазин. Обратитесь к администратору для создания магазина.')
else:
    print('Пользователя с таким логином не найдено в системе')
