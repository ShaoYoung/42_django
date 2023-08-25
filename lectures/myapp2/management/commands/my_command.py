from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello world!' to output."
    # обработчик
    def handle(self, *args, **kwargs):
        # вывод в консоль
        self.stdout.write('Hello world!')
