"""
Django settings for lectures project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-oh)l&b6lngk%-l$$#8-(y@h+h3_t01!^o(+r_mn51-dh3s$ts^'
# Секретный ключ. Его стоит хранить не в файле настроек, а в переменных окружения.
# Поэтому заменяем строку с ключом от Django на следующие пару строк
# getenv по ключу извлекает значение
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
# Режим отладки. Его необходимо отключить в готовом проекте.
# DEBUG = True
DEBUG = False


# Повышаем безопасность работы с сессиями и с csrf токенами
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# В константу ALLOWED_HOSTS файла settings.py необходимо добавить допустимые адреса в виде списка строк. Например так:
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.186.191',
    'ShaoYoung.pythonanywhere.com',
]

# В список INTERNAL_IPS добавим локальный адрес компьютера - 127.0.0.1.
# Панель DjDT отображается только в случае совпадения адреса.
INTERNAL_IPS = [
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # приложение myapp является частью проекта
    'myapp2',  # приложение myapp2 является частью проекта
    'myapp3',  # приложение myapp3 является частью проекта
    'myapp4',  # приложение myapp4 является частью проекта
    'myapp5',  # приложение myapp5 является частью проекта
    'myapp6',  # приложение myapp5 является частью проекта
    'debug_toolbar',    # приложение DjDT
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Рекомендуется подключить DebugToolbarMiddleware как можно раньше.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lectures.urls'

# Django позволяет создать базовый шаблон на уровне проекта. В таком случае все приложения смогут использовать его для расширения своих дочерних шаблонов.
# Для этого выполним предварительные настройки в файле settings.py проекта.
# Добавляем в список DIRS путь до каталога шаблона проекта -
# BASE_DIR / 'templates'.
# Далее создаём каталог templates в каталоге BASE_DIR. Это каталог верхнего уровня.
# В нём находится файл manage.py, каталог проекта и каталоги приложений
# TEMPLATES - это список, где django ищет файлы шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lectures.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ShaoYoung$default',
        'USER': 'ShaoYoung',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'ShaoYoung.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# настройка языка
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# путь до статики (css, js)
STATIC_URL = 'static/'
# константа для правильной настройки работы со статическими файлами на сервере. сбор всей статики в одном месте
STATIC_ROOT = BASE_DIR / 'static/'


# для сохранения изображений
# django создаёт (при первом использовании) эти каталоги и сохраняет в них изображения
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {'version': 1,
           'disable_existing_loggers': False,
           # форматы логирования
           'formatters': {
               # обычное форматирование
               'simple': {
                   # Добавляет вывод уровня предупреждения и само сообщение
                   'format': '%(levelname)s %(message)s'
               },
               # более крутое форматирование
               'verbose': {
                   'format': '{levelname} {asctime} {module} {process} {thread} {message}',
                   # стиль строки форматирования - фигурные скобки
                   'style': '{',
               },
           },
           # обработчики логирования
           'handlers': {
               # логирование в консоль
               'console': {
                   'class': 'logging.StreamHandler',
                   'formatter': 'verbose', # добавлен параметр formatter
               },
               # логирование в файл
               'file': {
                   'class': 'logging.FileHandler',
                   # 'filename': '/path/to/django.log',
                   'filename': './log/django.log',
                   'formatter': 'verbose', # добавлен параметр formatter
               },
           },
           'loggers': {
               # логирование всего django-сервера
               'django': {
                   # обработчики логирования (оба)
                   'handlers': ['console', 'file'],
                   'level': 'INFO',
               },
               # логирование приложения myapp
               'myapp': {
                   # обработчик - только консоль
                   # 'handlers': ['console'],
                   # обработчик - консоль и файл
                   'handlers': ['console', 'file'],
                   'level': 'DEBUG',
                   # если есть более вышестоящие логгеры, то их тоже используем
                   'propagate': True,
               },
           },
           }
# Освежить знания по логированию можно на странице официальной документации Python https://docs.python.org/3/library/logging.html


