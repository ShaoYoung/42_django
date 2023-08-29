from django.urls import path
from .views import get_articles
from .views import get_article
from .views import author_form
from .views import article_form
from .views import comment_form



urlpatterns = [
    path('articles/<int:author_id>/', get_articles),
    path('article/<int:article_id>/', get_article, name='article'),
    path('author/', author_form, name='author'),
    path('article/', article_form, name='article'),
    path('add_comment/<int:article_id>/', comment_form, name='add_comment'),
]

