from django.core.management import BaseCommand
from store_app.models import Product


class Command(BaseCommand):
    help = 'Create product'

    # передача нескольких параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product_name')
        parser.add_argument('description', type=str, help='Description')
        parser.add_argument('price', type=float, help='Price')
        parser.add_argument('quantity', type=int, help='Quantity')


    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
        )
        product.save()
        self.stdout.write('product created')

# python manage.py create_product milk milk 70.50 1
# python manage.py create_product bread bread 40.40 1

