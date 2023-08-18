from django.shortcuts import render
from django.http import HttpResponse  # HttpResponse - класс, к-й возвращает http-ответ от сервера клиенту
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logger.info('Index page was visited')
    return HttpResponse('Hello')

def about(request):
    logger.info('About page was visited')
    return HttpResponse('Something about us')



