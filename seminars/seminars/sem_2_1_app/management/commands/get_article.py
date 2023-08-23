from django.core.management import BaseCommand
from sem_2_1_app.models import Author, Article
from random import randint


class Command(BaseCommand):
    help = 'Get article by id'

    # передача двух параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.filter(pk=pk).first()
        self.stdout.write(f'{article}')
