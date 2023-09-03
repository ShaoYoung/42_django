from django.shortcuts import render
from django.views import View
# HttpResponse - это класс, экземпляры которого возвращают ответы
# JsonResponse - это класс, к-й позволяет возвращать ответ как json-объект
from django.http import HttpResponse, JsonResponse
# Чтобы передать данные в шаблон, мы можем использовать функцию render из модуля django.shortcuts:
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Author, Post
# get_object_or_404 позволяет обращаться к БД и получать объекты. Если нет, то django возвращает код 404
from django.shortcuts import get_object_or_404


# request - обязательная переменная
def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    # get или post запрос
    # request - обязательная переменная
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month} / {year} < br > {text}")


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее...    "
    }
    # возвращаем json-объект
    # json_dumps_params={'ensure_ascii': False} - для кодировки utf-8
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)


class TemplIf(TemplateView):
    # template_name - зарезервированное имя переменной. django будет искать шаблон именно здесь
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    # ключи должны иметь те имена, которые используются внутри шаблона
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)


def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/about.html')


def author_posts(request, author_id):
    # извлекаем автора или 404
    author = get_object_or_404(Author, pk=author_id)
    # order_by('-id') - сортировка по id в обратном порядке
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
