from django.contrib import admin

from .models import Coin, Author, Article, Comment

# регистрация моделей в административной панели сайта
admin.site.register(Coin)

