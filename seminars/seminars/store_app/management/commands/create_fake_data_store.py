from django.core.management import BaseCommand
from store_app.models import Client, Product, Order
from random import randint, choice, choices


class Command(BaseCommand):
    help = 'Create fake data in store'

    def handle(self, *args, **kwargs):
        # продукты
        products = ['bread', 'butter', 'milk', 'fish', 'meat', 'water', 'apple', 'banana', 'bagel', 'orange']
        # создаём фейковые продукты
        for i in range(10):
            product = Product(name=f'Product_{i+1}', description=f'{choice(products)}', price=randint(50, 500), quantity=randint(1,3))
            product.save()
        # города
        cities = ['Tomsk', 'Moscow', 'New_York', 'Novosibirsk', 'Kathmandu']
        # создаём фейковых клиентов
        for i in range(10):
            client = Client(name=f'Client_{i + 1}', email=f'client_{i + 1}@mail.ru', phone=f'+790000000{i}{i}',
                            address=f'{choice(cities)}')
            client.save()
        # продукты (объекты)
        products = [*Product.objects.all()]
        # создаём фейковые заказы для каждого клиента
        for client in Client.objects.all():
            # кол-во заказов у клиента от 1 до 5
            for _ in range(randint(1, 6)):
                order = Order(client=client, sum_order=0, date_create=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
                order.save()
                order_sum = 0
                # кол-во товаров в заказе от 1 до 5
                order_products = choices(products, k=randint(1, 5))

                for product in order_products:
                    # сумма товаров в заказе
                    order_sum += product.price

                # ManyToManyField заполняется после записи order
                # добавляем продукты в заказ
                order.products.set(order_products)
                order.sum_order = order_sum
                order.save()




