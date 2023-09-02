from django.contrib import admin

from .models import Client, Product, Order


# Создаём класс ProductAdmin как дочерний для admin.ModelAdmin. Он позволит изменить работу с продуктами в админке,
# не меняя модель Продукты. Следовательно, нам не надо делать миграции, вносить изменения в базу данных.
class ClientAdmin(admin.ModelAdmin):
    # список
    # отображение дополнительных полей списка
    list_display = ['name', 'email', 'phone']
    # сортировка списка по имени (по возрастанию)
    ordering = ['name']
    # список для фильтрации
    list_filter = ['name']
    # подсказка для поля поиска
    search_help_text = 'Поиск клиента по имени'

    # объект
    # отображение полей объекта
    fields = ['name', 'email', 'phone', 'date_reg']
    # поля объекта только для чтения
    readonly_fields = ['name', 'date_reg']


class ProductAdmin(admin.ModelAdmin):
    # список
    # отображение дополнительных полей списка
    list_display = ['name', 'description', 'price']
    # сортировка списка по названию (по алфавиту)
    ordering = ['name']
    # список для фильтрации
    list_filter = ['name']
    # подсказка для поля поиска
    search_help_text = 'Поиск продукта по названию'

    # объект
    # отображение полей объекта
    fields = ['name', 'description', 'price', 'quantity', 'image']
    # поля объекта только для чтения
    readonly_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    # список
    # отображение дополнительных полей списка
    list_display = ['client', 'sum_order', 'date_create']
    # сортировка списка по дате создания (по убыванию)
    ordering = ['-date_create']
    # список для фильтрации
    list_filter = ['client']
    # подсказка для поля поиска
    search_help_text = 'Поиск заказа по клиенту'

    # объект
    # отображение полей объекта
    fields = ['client', 'products', 'sum_order', 'date_create']
    # поля объекта только для чтения
    readonly_fields = ['date_create']


# регистрация моделей в административной панели сайта
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
