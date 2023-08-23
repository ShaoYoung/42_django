from django.core.management.base import BaseCommand
from sem_2_1_app.models import Author
from datetime import datetime


class Command(BaseCommand):
    help = 'Create authors'
    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(name=f'name_{i}', surname=f'surname_{i}', email=f'email_{i}@mail.ru',
                            biography='bla_bla_bla')
            author.save()
        self.stdout.write('authors created')


