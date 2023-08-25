from django.urls import path
# импортируем два представления из view
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import TemplIf
from .views import view_for
from .views import index, about
from .views import author_posts, post_full


urlpatterns = [
    path('hello/', hello, name='hello'),
    # при вызове класса особый синтаксис
    path('hello2/', HelloView.as_view(), name='hello2'),

    # django ищет совпадение
    # year передаётся в year_post
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),

]

# В Django преобразование путей осуществляется с помощью приставок, которые определяют тип данных, который будет
# передаваться в качестве параметра в представление. Для этого мы заключаем параметр в треугольные скобки и
# указываем приставку, а далее после двоеточия слитно пишем имя параметра.
# ● str — приставка для передачи строки любых символов, кроме слэша.
# Например, если мы хотим передать в представление информацию о
# конкретном посте блога, то мы можем использовать такой путь:
# path('posts/<str:slug>/', post_detail). Здесь slug - это строка символов, которая
# является уникальным идентификатором поста.
# ● int — приставка для передачи целого числа. Например, если мы хотим
# передать в представление информацию о конкретном пользователе по его
# идентификатору, то мы можем использовать такой путь:
# path('users/<int:id>/', user_detail). Здесь id - это целое число, которое является
# уникальным идентификатором пользователя.
# ● slug — приставка для передачи строки, содержащей только буквы, цифры,
# дефисы и знаки подчеркивания. Например, если мы хотим передать в
# представление информацию о конкретной категории товаров, то мы можем
# использовать такой путь:
# path('categories/<slug:slug>/', category_detail). Здесь slug - это строка
# символов, которая является уникальным идентификатором категории.
# ● uuid — приставка для передачи уникального идентификатора. Например, если
# мы хотим передать в представление информацию о конкретном заказе, то мы
# можем использовать такой путь:
# path('orders/<uuid:pk>/', order_detail). Здесь pk - это уникальный
# идентификатор заказа.
# ● path — приставка для передачи строки любых символов, включая слэши.
# Например, если мы хотим передать в представление информацию о
# конкретном файле на сервере, то мы можем использовать такой путь:
# path('files/<path:url>/', file_detail). Здесь url - это строка символов, которая
# содержит путь к файлу на сервере.
