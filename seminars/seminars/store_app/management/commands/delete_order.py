from django.core.management import BaseCommand
from store_app.models import Client, Order


class Command(BaseCommand):
    help = 'delete orders by client name'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str, help='client name')

    def handle(self, *args, **kwargs):
        client_name = kwargs.get('client')
        client = Client.objects.filter(name=client_name).first()
        # print(client.name)
        if client:
            orders = Order.objects.filter(client=client)
            for order in orders:
                order.delete()
                self.stdout.write(f'order {order} deleted')

# python manage.py delete_order ivan
# python manage.py delete_order maria
