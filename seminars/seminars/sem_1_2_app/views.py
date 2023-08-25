from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging
from django.shortcuts import render

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

