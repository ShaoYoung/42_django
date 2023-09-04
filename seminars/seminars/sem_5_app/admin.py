from django.contrib import admin

from sem_2_1_app.models import Author, Article, Comment
# ..sem_2_1_app.models import Author, Article, Comment

# @admin.action(description="Сбросить количество в ноль")
# def reset_quantity(modeladmin, request, queryset):
#     queryset.update(quantity=0)

# Создаём класс ProductAdmin как дочерний для admin.ModelAdmin. Он позволит изменить работу с продуктами в админке,
# не меняя модель Продукты. Следовательно, нам не надо делать миграции, вносить изменения в базу данных.
class AuthorAdmin(admin.ModelAdmin):
    # отображение дополнительных полей
    list_display = ['name', 'email']
    # сортировка по убыванию (-quantity)
    ordering = ['name']
   # отображение полей
    fields = ['name', 'surname', 'email', 'biography', 'birthday']
    # поля только для чтения
    readonly_fields = ['name', 'surname', 'birthday']

class ArticleAdmin(admin.ModelAdmin):
    # отображение дополнительных полей
    list_display = ['head', 'content', 'author']
    # сортировка по убыванию (-quantity)
    ordering = ['head']
    # отображение полей
    fields = ['head', 'content', 'author', 'public_date']
    # поля только для чтения
    readonly_fields = ['head', 'public_date', 'author']


class CommentAdmin(admin.ModelAdmin):
    # отображение дополнительных полей
    list_display = ['author', 'article']
    # отображение полей
    fields = ['author', 'article', 'content', 'make_date']
    # поля только для чтения
    readonly_fields = ['author', 'article', 'make_date']


    # сортировка по убыванию (-quantity)
    # ordering = ['name']
    # # список для фильтрации
    # list_filter = ['birthday']
    # # поле для поиска
    # search_fields = ['name']
    # # подсказка для поля для поиска
    # search_help_text = 'Поиск по полю name'
    # # подключение функции reset_quantity к actions (передаётся функция, а не её имя)
    # actions = [reset_quantity]


# регистрация моделей в административной панели сайта
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

