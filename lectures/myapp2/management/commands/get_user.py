from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    # для передачи параметра id в командной строке. Метод add_arguments позволяет парсить командную строку.
    def add_arguments(self, parser):
        # parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        # id = kwargs['id']
        # # при запросе несуществующего id будет вызвано исключение. Чтобы исключить это, надо использовать метод filter
        # user = User.objects.get(id=id)
        # self.stdout.write(f'{user}')
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
