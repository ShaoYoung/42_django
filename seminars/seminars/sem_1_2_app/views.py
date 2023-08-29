from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
import logging
from django.shortcuts import render
from .forms import ChoiceForm

logger = logging.getLogger(__name__)

# Create your views here.

def coin(request):
    throw = randint(0, 1)
    throw = 'Решка' if throw else 'Орёл'
    # logger.info(f'Coin throw result - {throw}')
    context = {'result': throw}
    return render(request, 'sem_1_2_app/temp_1.html', context)


def cube(request):
    throw = randint(1, 6)
    context = {'result': throw}
    return render(request, 'sem_1_2_app/temp_1.html', context)


def rand100(request):
    random_number = randint(0, 100)
    context = {'result': random_number}
    return render(request, 'sem_1_2_app/temp_1.html', context)


def choice(request):
    # если получен post-запрос (пользователь ввёл данные в форму и нажал кнопку "Отправить"
    if request.method == 'POST':
        # создаётся экземпляр класса, который заполняется данными из формы, к-е ввёл пользователь
        form = ChoiceForm(request.POST)
        # если данные формы прошли валидацию
        if form.is_valid():
            # извлечение данных из формы. обращение как к элементам словаря
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'd':
                return cube(request)
                # redirect('dice', count=count)
            elif game == 'r':
                return rand100(request)
            elif game == 'c':
                return coin(request)
    else:
        form = ChoiceForm()
        # создаётся экземпляр класса, который получит пользователь при отправке get-запроса
    return render(request, 'sem_1_2_app/choice.html', {'form': form})




