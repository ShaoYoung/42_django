"""
URL configuration for seminars project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sem_1_1_app.urls')),
    path('sem_1_1/', include('sem_1_1_app.urls')),
    path('sem_1_2/', include('sem_1_2_app.urls')),
    path('hw_1/', include('homework_1_app.urls')),
]

