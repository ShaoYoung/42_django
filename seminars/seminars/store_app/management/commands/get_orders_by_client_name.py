from django.core.management import BaseCommand
from store_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'get orders by client name'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str, help='client name')

    def handle(self, *args, **kwargs):
        client_name = kwargs.get('client')
        client = Client.objects.filter(name=client_name).first()
        # print(client.name)
        if client:
            orders = Order.objects.filter(client=client)
            intro = f'All orders of client {client.name}\n'
            text = '\n'.join(f'{order.id=}  {order.sum_order=}  {order.products.name}' for order in orders)
            self.stdout.write(f'{intro}{text}')

# python manage.py get_orders_by_client_name ivan
# python manage.py get_orders_by_client_name maria
