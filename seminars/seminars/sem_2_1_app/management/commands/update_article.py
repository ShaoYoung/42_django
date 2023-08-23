from django.core.management import BaseCommand
from sem_2_1_app.models import Author, Article
from random import randint


class Command(BaseCommand):
    help = 'Update article head by ID'

    # передача двух параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('head', type=str, help='Article head')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        head = kwargs.get('head')
        article = Article.objects.filter(pk=pk).first()
        article.head = head
        article.save()
        self.stdout.write(f'{article}')