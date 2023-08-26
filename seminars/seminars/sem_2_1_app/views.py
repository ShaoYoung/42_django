from django.views import View
# HttpResponse - это класс, экземпляры которого возвращают ответы
# JsonResponse - это класс, к-й позволяет возвращать ответ как json-объект
from django.http import HttpResponse, JsonResponse
# Чтобы передать данные в шаблон, мы можем использовать функцию render из модуля django.shortcuts:
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Author, Article, Comment
# get_object_or_404 позволяет обращаться к БД и получать объекты. Если нет, то django возвращает код 404
from django.shortcuts import get_object_or_404


def get_articles(request, author_id):
    # print(author_id)
    articles = Article.objects.filter(author__pk=author_id)
    # print(len(articles))
    context = {"articles": articles}
    return render(request, "sem_2_1_app/articles.html", context)


def get_article(request, article_id):
    article = Article.objects.filter(pk=article_id).first()
    article.count += 1
    article.save()
    # все комментарии статьи
    comments = Comment.objects.filter(article=article).order_by('modify_date')
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, "sem_2_1_app/article.html", context)

