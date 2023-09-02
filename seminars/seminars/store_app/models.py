from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}, телефон: {self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now=True)
    # upload_to - директория в media, куда будет сохраняться изображения
    image = models.ImageField(upload_to='product_media/', default=None)

    def __str__(self):
        return f'Товар: {self.name}, описание: {self.description}, цена: {self.price}'


class Order(models.Model):
    # клиент может иметь несколько заказов, но у заказа должен быть конкретный клиент. Один ко многим
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Заказ может содержать несколько товаров. Товар может входить в несколько заказов. Список ManyToManyField ?!?
    products = models.ManyToManyField(Product)
    sum_order = models.DecimalField(max_digits=15, decimal_places=2)
    date_create = models.DateField()
