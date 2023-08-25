from django.urls import path
from .views import get_articles
from .views import get_article


urlpatterns = [
    path('articles/<int:author_id>/', get_articles),
    path('article/<int:article_id>/', get_article, name='article'),

]

