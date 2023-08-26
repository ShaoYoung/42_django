from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Client, Product, Order
from datetime import datetime, timedelta


def get_orders_by_client_id(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    # print(client)
    # все заказы клиента
    orders = Order.objects.filter(client=client)
    # print(orders)
    # заказы с товарами
    orders_with_products = {}
    for order in orders:
        products = Order.objects.get(id=order.id).products.all()
        # ключ - заказ, значение - товары этого заказа
        orders_with_products[order] = products

    context = {
        'client': client,
        'orders': orders_with_products,
    }
    return render(request, "store_app/client_orders.html", context)

def get_products_by_client_id(request, client_id: int, period: str):
    client = Client.objects.filter(pk=client_id).first()
    current_time = datetime.now()
    if period.lower() == 'hour':
        time_filter = current_time - timedelta(hours=1)
    elif period.lower() == 'week':
        time_filter = current_time - timedelta(weeks=1)
    elif period.lower() == 'month':
        time_filter = current_time - timedelta(days=30)
    elif period.lower() == 'year':
        time_filter = current_time - timedelta(days=365)
    else:
        time_filter = current_time - timedelta(days=365*100)
    # print(time_filter)

    # заказы клиента с датой создания >= условной даты
    orders = Order.objects.filter(client=client, date_create__gte=time_filter)
    # print(orders)
    products = []

    for order in orders:
        # расширяем список товаров
        products.extend(Order.objects.get(id=order.id).products.all())
        # print(order.date_create)

    context = {
        'client': client,
        # исключаем повторяющиеся товары
        'products': set(products),
    }
    return render(request, "store_app/client_products.html", context)

