from django.urls import path
from . import views

# получаем доступ к views
# по пустому пути импортируется функция index
# по пути about/ импортируется функция about
urlpatterns = [path('', views.index, name='index'), path('about/', views.about, name='about'), ]


