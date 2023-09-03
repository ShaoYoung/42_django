from django.contrib import admin

from .models import Author, Post

# регистрация моделей в административной панели сайта
admin.site.register(Author)
admin.site.register(Post)
