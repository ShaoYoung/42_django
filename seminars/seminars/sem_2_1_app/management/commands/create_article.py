from django.core.management import BaseCommand
from sem_2_1_app.models import Author, Article
from random import randint


class Command(BaseCommand):
    help = 'Create article'

    # передача двух параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('head', type=str, help='Article_head')
        parser.add_argument('auth_id', type=int, help='Author')


    def handle(self, *args, **kwargs):
        head = kwargs.get('head')
        auth_id = kwargs.get('auth_id')
        author = Author.objects.filter(pk=auth_id).first()
        # print(author)
        article = Article(
            head=head,
            content='random_bla-bla-bla',
            author=author,
            category='category',
            public=randint(0, 1),
        )
        # print(article)
        article.save()
        self.stdout.write('article created')