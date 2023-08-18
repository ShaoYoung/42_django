from django.urls import path
from . import views

# получаем доступ к views
# по пустому пути импортируется функция main
# по пути about/ импортируется функция about
urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
]