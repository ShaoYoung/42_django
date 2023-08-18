from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def coin(request):
    throw = randint(0, 1)
    throw = 'Решка' if throw else 'Орёл'
    logger.info(f'Coin throw result - {throw}')
    return HttpResponse(f'Результат - {throw}')


def cube(request):
    throw = randint(1, 6)
    logger.info(f'Cube throw - {throw}')
    return HttpResponse(f'На кубике выпало - {throw}')


def rand100(request):
    random_number = randint(0, 100)
    logger.info(f'Random number {random_number}')
    return HttpResponse(f'Случайное число {random_number}')

