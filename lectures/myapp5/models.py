from django.db import models


class Category(models.Model):
    # unique=True - поле должно быть уникально
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # blank=True - обязательное для заполнения поле
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

    # декоратор @property. Декорируемый метод total_quantity надо воспринимать не как метод, а как свойство экземпляра
    @property
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all())
