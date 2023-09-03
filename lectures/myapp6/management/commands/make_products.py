from random import choice, randint, uniform
from django.core.management.base import BaseCommand
# В реальном проекте приложения не должны иметь тесной связи между собой
from myapp5.models import Category, Product
# from lectures.myapp5.models import Category, Product
# from myapp5.models import Category, Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продуктов для генерации')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'продукт номер {i}',
                category=choice(categories),
                description='длинное описание продукта, которое и так никто не читает',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        #     Вместо метода save для сохранения каждого продукта по отдельности, используем метод bulk_create.
        #     Он получает список продуктов и сохраняет его в базу данных одной операцией.
        print(f'{count} products added to DB.')
        Product.objects.bulk_create(products)
