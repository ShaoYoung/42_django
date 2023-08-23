from django.core.management import BaseCommand
from sem_2_1_app.models import Article


class Command(BaseCommand):
    help = 'Delete article by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.filter(pk=pk).first()
        if article:
            article.delete()
        self.stdout.write(f'{article}')
