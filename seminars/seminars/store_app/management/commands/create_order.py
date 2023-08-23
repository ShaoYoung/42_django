from django.core.management import BaseCommand
from store_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Create order'

    # передача нескольких параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='client_id')
        parser.add_argument('product', type=int, help='product_id')
        parser.add_argument('quantity', type=int, help='quantity')


    def handle(self, *args, **kwargs):
        client_id = kwargs.get('client')
        client = Client.objects.filter(pk=client_id).first()
        product_id = kwargs.get('product')
        product = Product.objects.filter(pk=product_id).first()
        quantity = kwargs.get('quantity')
        sum_order = product.price * quantity
        order = Order(
            client=client,
            sum_order=sum_order,
        )
        order.save()
        # ManyToManyField заполняется после записи order
        order.products.create(name=product.name, description=product.description, price=product.price, quantity=product.quantity, date_add=product.date_add)
        # order.products.set(name=product.name, description=product.description, price=product.price, quantity=product.quantity, date_add=product.date_add)
        order.save()
        self.stdout.write('order created')

# python manage.py create_order 1 1 1
# python manage.py create_order 2 2 2
