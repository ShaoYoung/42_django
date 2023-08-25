from django.db import models


# если указан параметр "blank=False" - поле обязательно для заполнения
# Полный список всех полей Django доступен по ссылке:
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types

# Класс должен иметь то имя, которое будет использоваться для таблицы в БД
class User(models.Model):
    # атрибуты класса - названия столбцов таблицы User
    # id создавать не надо, django добавляет его автоматически
    # CharField - поле для хранения строк (букв)
    name = models.CharField(max_length=100)
    # EmailField - поле для хранения электронных адресов. Django проверяет корректность введённого адреса
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # IntegerField - int
    age = models.IntegerField()

    # дандер метод для вывода
    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # TextField - текстовое поле
    description = models.TextField()
    # ImageField - для хранения изображений. Файлы хранятся в products/, image хранит ссылки на файлы
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    # ссылка на User, on_delete=models.CASCADE - при удалении User будут удалены и его заказы
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # auto_now_add=True - автоматическое добавление при добавлении Order
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    # пользовательский метод. возврат первых 8 слов контента
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'