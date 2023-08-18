from django.shortcuts import render
from django.http import HttpResponse  # HttpResponse - класс, к-й возвращает http-ответ от сервера клиенту
import logging
from functools import wraps
from datetime import datetime

logger = logging.getLogger(__name__)


def write_log(func):
    @wraps(func)
    def wrapper(request):
        view_name = func.__name__
        # print(view_name)
        client_ip = get_client_ip(request)
        # print(client_ip)
        logger.info(f'=== Page "{view_name}" was visited from ip = {client_ip}')
        return func(request)

    return wrapper


@write_log
def main(request):
    html_text = "<h1>My name is Shaverin Nikita.</h1>" \
                "<h2>I'm forty four years old.</h2>" \
                "<h2>I live in Tomsk city.</h2>" \
                "<h3>I'm learning in GeekBrains on the faculty of Python developer more than year yet.</h3>"
    return HttpResponse(html_text)


@write_log
def about(request):
    html_text = f"<h1>Now i'm learning very interesting Django framework.</h1>" \
                f"<h2>I can make something yet.</h2>" \
                f"<h2>For example:</h2>" \
                f"<ul>" \
                f"<li>Now is {datetime.now().strftime('%H:%M - %d.%m.%Y y.')}</li>" \
                f"<li>You visited this site from IP {get_client_ip(request)}</li>" \
                f"</ul>" \
                f"<h3>It's only the beginning!</h3>"
    return HttpResponse(html_text)


# возвращает ip, с которого пришёл request
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # если ip передан через proxy
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    # если открыто
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
