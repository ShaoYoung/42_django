from django.core.management import BaseCommand
from sem_2_1_app.models import Author, Comment


class Command(BaseCommand):
    help = 'Get comments by author name'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Authors name')
        parser.add_argument('sort', type=str, help='Sort')
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        sort = kwargs.get('sort')
        count = kwargs.get('count')
        author = Author.objects.filter(name=name).first()
        # если автор найден
        if author is not None:
            # извлекаем все статьи. Получаем QuerySet. Можно работать как со списком list
            # order_by - сортировка по полю, [:count] - первые count QuerySet
            # если sort есть в Comment
            if sort in dir(Comment):
                comments = Comment.objects.filter(author=author).order_by(sort)[:count]
            else:
                # print('unsorted')
                comments = Comment.objects.filter(author=author)[:count]
            intro = f'All comments of author {author.name}\n'
            # собираем строку через set comprehension
            text = '\n'.join(comment.content for comment in comments)
            self.stdout.write(f'{intro}{text}')


