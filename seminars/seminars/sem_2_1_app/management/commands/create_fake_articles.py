from django.core.management.base import BaseCommand
from sem_2_1_app.models import Author, Article, Comment
from random import randint, choice


class Command(BaseCommand):
    help = 'Fill db by fake data'

    def handle(self, *args, **options):
        for i in range(5):
            author = Author(name=f'Name{i + 1}', surname=f'Surname{i + 1}', email=f'name_surname{i + 1}@gmail.com',
                            birthday=f'{randint(1700, 1950)}-{randint(1, 12)}-{randint(1, 28)}',
                            biography='Some biography')
            author.save()
            for j in range(1, 4):
                article = Article(head=f'Title{i * 3 + j}', content='Some content', category='SomeCategory', author=author, public=randint(0,1))
                article.save()

        authors = [*Author.objects.all()]
        for article in Article.objects.all():
            for i in range(3):
                comment = Comment(author=choice(authors), article=article, content='Some comment')
                comment.save()

