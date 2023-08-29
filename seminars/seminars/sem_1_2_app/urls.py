from django.urls import path
from . import views

# получаем доступ к views
# по пустому пути импортируется функция index
# по пути about/ импортируется функция about
urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('rand100/', views.rand100, name='rand100'),
    path('choice/', views.choice, name='choice'),

]

