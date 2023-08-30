from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Client, Product, Order
from datetime import datetime, timedelta
from .forms import EditProductForm
from django.core.files.storage import FileSystemStorage


def get_product_by_id(request, product_id):
    product = Product.objects.filter(pk=product_id).first()

    print(product)
    print(product.image)
    context = {
        'title': 'Продукт',
        'message': 'Описание продукта',
        'product': product,
    }
    return render(request, "store_app/product.html", context)



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
        time_filter = current_time - timedelta(days=365 * 100)
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


def edit_product(request):
    message = 'Продукт не был изменён'
    # если получен post-запрос (пользователь ввёл данные в форму и нажал кнопку "Отправить"
    if request.method == 'POST':
        # создаётся экземпляр класса, который заполняется данными из формы, к-е ввёл пользователь
        form = EditProductForm(request.POST, request.FILES)
        # если данные формы прошли валидацию
        if form.is_valid():
            # изменяемый продукт
            edited_product = form.cleaned_data['edited_product']
            # print(edited_product)
            if form.cleaned_data['name']:
                edited_product.name = form.cleaned_data['name']
                message = 'Продукт изменён'
            if form.cleaned_data['description']:
                edited_product.description = form.cleaned_data['description'],
                message = 'Продукт изменён'
            if form.cleaned_data['price']:
                edited_product.price = form.cleaned_data['price']
                message = 'Продукт изменён'
            if form.cleaned_data['quantity']:
                edited_product.quantity = form.cleaned_data['quantity']
                message = 'Продукт изменён'
            if form.cleaned_data['date_add']:
                edited_product.date_add = form.cleaned_data['date_add']
                message = 'Продукт изменён'
            if form.cleaned_data['image']:
                # извлекаем изображение из формы по ключу image
                image = form.cleaned_data['image']
                # создаём экземпляр класса FileSystemStorage (позволяет работать с файлами, файловой системой)
                fs = FileSystemStorage()
                # сохраняем файл по имени image.name объект image
                fs.save(image.name, image)
                edited_product.image = image
                message = 'Продукт изменён'

            if message == 'Продукт изменён':
                edited_product.save()
    else:
        message = 'Выберите продукт и задайте новые значения его свойств. Не заполненные поля не обновятся.'
        form = EditProductForm()
        # создаётся экземпляр класса, который получит пользователь при отправке get-запроса
    return render(request, 'store_app/edit_product.html',
                  {'form': form, 'message': message, 'title': 'Изменение продукта, добавление фотографии'})
