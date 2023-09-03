import logging
# render для отрисовки html
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def user_form(request):
    # если получен post-запрос (пользователь ввёл данные в форму и нажал кнопку "Отправить"
    if request.method == 'POST':
        # создаётся экземпляр класса, который заполняется данными из формы, к-е ввёл пользователь
        form = UserForm(request.POST)
        # если данные формы прошли валидацию
        if form.is_valid():
            # извлечение данных из формы. обращение как к элементам словаря
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            # print(f'Получили {name=}, {email=}, {age=}.')
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        # создаётся экземпляр класса, который получит пользователь при отправке get-запроса
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST)
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            print(f'Получили {form.cleaned_data=}.')
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        # form = ManyFieldsForm()
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        # POST - для сохранения текстовой информации, FILES - для сохранения набора байт, к-й идёт от клиента на сервер
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # извлекаем изображение из формы по ключу image
            image = form.cleaned_data['image']
            # создаём экземпляр класса FileSystemStorage (позволяет работать с файлами, файловой системой)
            fs = FileSystemStorage()
            # сохраняем файл по имени image.name объект image
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})


