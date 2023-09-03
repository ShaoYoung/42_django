from django.contrib import admin

from .models import Category, Product


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


# Создаём класс ProductAdmin как дочерний для admin.ModelAdmin. Он позволит изменить работу с продуктами в админке,
# не меняя модель Продукты. Следовательно, нам не надо делать миграции, вносить изменения в базу данных.
class ProductAdmin(admin.ModelAdmin):
    # отображение дополнительных полей
    list_display = ['name', 'category', 'quantity']
    # сортировка по убыванию (-quantity)
    ordering = ['category', '-quantity']
    # список для фильтрации
    list_filter = ['date_added', 'price']
    # поле для поиска
    search_fields = ['description']
    # подсказка для поля для поиска
    search_help_text = 'Поиск по полю Описание продукта (description)'
    # подключение функции reset_quantity к actions (передаётся функция, а не её имя)
    actions = [reset_quantity]

    """Отдельный продукт."""
    # отображение полей
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    # поля только для чтения
    readonly_fields = ['date_added', 'rating']
    # детальная настройка отображения полей (не дружит с fields)
    fieldsets = [
        (
            None,
            {
                # широко
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                # поле схлопывается
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                # те поля из БД, к-е схлопывваются
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
        ]


# регистрация моделей в административной панели сайта
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)




