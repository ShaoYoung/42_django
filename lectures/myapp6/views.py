from django.shortcuts import render
# Sum - подсчёт агрегированных показателей
from django.db.models import Sum
from myapp5.models import Product


# вычисление сумма непосредственно в БД посредством запроса
def total_in_db(request):
    # используется агрегатный метод aggregate
    # Метод aggregate(Sum('quantity')) отправит в базу агрегирующий запрос с суммированием всех значений столбца “количество”
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


# вычисление суммы в представлении
def total_in_view(request):
    # получаем все продукты из базы
    products = Product.objects.all()
    # суммируем поля product.quantity
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


# вычисление суммы в шаблоне
def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
