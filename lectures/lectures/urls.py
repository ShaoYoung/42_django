"""
URL configuration for lectures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # include - для подключения
from myapp3.views import index

# шаблоны адресов
urlpatterns = [
    path('admin/', admin.site.urls),
    # по пути <ip-address:port> подключается приложение myapp
    # path('', include('myapp.urls')),
    # для проверки работоспособности
    path('prefix/', include('myapp.urls')),
    # по пути lec3 подключается приложение myapp3 (далее его view)
    path('les3/', include('myapp3.urls')),
    path('', index),
]
