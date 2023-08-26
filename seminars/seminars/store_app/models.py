from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now=True)


class Order(models.Model):
    # клиент может иметь несколько заказов, но у заказа должен быть конкретный клиент. Один ко многим
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Заказ может содержать несколько товаров. Товар может входить в несколько заказов. Список ManyToManyField ?!?
    products = models.ManyToManyField(Product)
    sum_order = models.DecimalField(max_digits=15, decimal_places=2)
    date_create = models.DateField()

