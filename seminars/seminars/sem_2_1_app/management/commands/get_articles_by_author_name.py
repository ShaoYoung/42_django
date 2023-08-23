from django.core.management import BaseCommand
from sem_2_1_app.models import Author, Article


class Command(BaseCommand):
    help = 'Get article by author name'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Authors name')
        parser.add_argument('sort', type=str, help='Sort')
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        sort = kwargs.get('sort')
        count = kwargs.get('count')
        author = Author.objects.filter(name=name).first()
        if author is not None:
            # извлекаем все статьи. Получаем QuerySet. Можно работать как со списком list
            # order_by - сортировка по полю, [:count] - первые count QuerySet
            # если sort есть в Article
            if sort in dir(Article):
                articles = Article.objects.filter(author=author).order_by(sort)[:count]
            else:
                # print('unsorted')
                articles = Article.objects.filter(author=author)[:count]
            intro = f'All articles of author {author.name}\n'
            # собираем строку через set comprehension
            text = '\n'.join(article.head for article in articles)
            self.stdout.write(f'{intro}{text}')


