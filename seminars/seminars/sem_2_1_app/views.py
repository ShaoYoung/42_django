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
from .forms import AuthorForm, ArticleForm, CommentForm


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


def author_form(request):
    message = ''
    # если получен post-запрос (пользователь ввёл данные в форму и нажал кнопку "Отправить"
    if request.method == 'POST':
        # создаётся экземпляр класса, который заполняется данными из формы, к-е ввёл пользователь
        form = AuthorForm(request.POST)
        # если данные формы прошли валидацию
        if form.is_valid():
            author = Author(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                biography=form.cleaned_data['biography'],
                birthday=form.cleaned_data['birthday'],
            )
            author.save()
            message = 'Автор сохранён'
    else:
        form = AuthorForm()
        # создаётся экземпляр класса, который получит пользователь при отправке get-запроса
    return render(request, 'sem_2_1_app/author.html', {'form': form, 'message': message, 'title': 'Сохранение автора'})


def article_form(request):
    message = ''
    # если получен post-запрос (пользователь ввёл данные в форму и нажал кнопку "Отправить"
    if request.method == 'POST':
        # создаётся экземпляр класса, который заполняется данными из формы, к-е ввёл пользователь
        form = ArticleForm(request.POST)
        # если данные формы прошли валидацию
        if form.is_valid():
            article = Article(
                head=form.cleaned_data['head'],
                content=form.cleaned_data['content'],
                author=form.cleaned_data['author'],
                category=form.cleaned_data['category'],
            )
            article.save()
            message = 'Статья сохранёна'
    else:
        form = ArticleForm()
        # создаётся экземпляр класса, который получит пользователь при отправке get-запроса
    return render(request, 'sem_2_1_app/author.html', {'form': form, 'message': message, 'title': 'Сохранение статьи'})


def comment_form(request, article_id):
    message = ''
    # ищем статью по её id
    article = Article.objects.filter(pk=article_id).first()
    # все комментарии статьи
    comments = Comment.objects.filter(article=article).order_by('modify_date')

    # если получен post-запрос (пользователь ввёл данные в форму и нажал кнопку "Отправить"
    if request.method == 'POST':
        # создаётся экземпляр класса, который заполняется данными из формы, к-е ввёл пользователь
        form = CommentForm(request.POST)
        # если данные формы прошли валидацию
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                content=form.cleaned_data['comment'],
                article=Article.objects.filter(pk=article_id).first()
            )
            comment.save()
            message = 'Комментарий сохранён'
    else:
        form = CommentForm()
        # создаётся экземпляр класса, который получит пользователь при отправке get-запроса
    return render(request, 'sem_2_1_app/add_comment.html', {'form': form, 'message': message, 'title': 'Сохранение комментария', 'article': article, 'comments': comments})


