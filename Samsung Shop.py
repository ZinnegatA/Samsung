class Shop:
    boughtItems = []
    products = []

    def __init__(self, name):
        self.name = name

    def add_products(self, *products):
        Shop.products.extend(products)

    def del_product(self, product):
        Shop.products.remove(product)
        print('Продукт удален из магазина')


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
        self.wallet = wallet
        self.cart = Cart()

    def buy_product(self, product):
        Cart.items.append(product)
        Cart.total_amount += product.price
        self.wallet -= product.price
        print(f'''В кошельке осталось {self.wallet} средств
В корзине на данный момент товаров на {Cart.total_amount}''')

    def __str__(self):
        return f'Имя покупателя: {self.name}, средств на кошельке: {self.wallet}'


mobile = Electroproducts('Мобильник', 100)
bear = Toys('Мишка', 50)

shop = Shop('Радуга')
shop.add_products(mobile, bear)
print(shop.products)
me = Buyer('Руслан', 500)
me.buy_product(mobile)
print(me.cart.items)
