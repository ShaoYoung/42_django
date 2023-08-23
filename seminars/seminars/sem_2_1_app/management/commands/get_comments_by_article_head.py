from django.core.management import BaseCommand
from sem_2_1_app.models import Comment, Article


class Command(BaseCommand):
    help = 'Get comments by article head'

    def add_arguments(self, parser):
        parser.add_argument('head', type=str, help='Article head')
        parser.add_argument('sort', type=str, help='Sort')
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **kwargs):
        head = kwargs.get('head')
        sort = kwargs.get('sort')
        count = kwargs.get('count')
        article = Article.objects.filter(head=head).first()
        # если автор найден
        if article is not None:
            # извлекаем все статьи. Получаем QuerySet. Можно работать как со списком list
            # order_by - сортировка по полю, [:count] - первые count QuerySet
            # если sort есть в Article
            if sort in dir(Article):
                comments = Comment.objects.filter(article=article).order_by(sort)[:count]
            else:
                # print('unsorted')
                comments = Comment.objects.filter(article=article)[:count]
            intro = f'All comments of article {article.head}\n'
            # собираем строку через set comprehension
            text = '\n'.join(comment.content for comment in comments)
            self.stdout.write(f'{intro}{text}')


