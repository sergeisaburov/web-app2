"""
Описываются все глобальные настройки для джанго проекта
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
""" Прописывается полный путь к проекту   """
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k9p10_@o(5g!_kzip(7wx^6lx=zz%rfk^@-y!!+ai$f6#^tjzf'

# SECURITY WARNING: don't run with debug turned on in production!
""" Если TRUE то режим разработчика  """
DEBUG = True
""" Указываются доменные имена, где публикуется сайт , например  ALLOWED_HOSTS = [https://itproger.com]"""
ALLOWED_HOSTS = []
""" Набор всех установленных приложений, которые есть в проекте """
INSTALLED_APPS = [
    'main',  # Регистрация созданного приложения
    'django.contrib.admin',  # Приложение - панель администратора
    'django.contrib.auth',  #
    'django.contrib.contenttypes',  #
    'django.contrib.sessions',  # Приложение - по работе с сессиями
    'django.contrib.messages',  # Приложение - по работе с сообщениями
    'django.contrib.staticfiles',  # Приложение - по работе с статическими файлами
]
""" Различное промежуточное Прогр.Обеспеч. """
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # обеспечивает безопасность внутри проекта
    'django.contrib.sessions.middleware.SessionMiddleware',  # обеспечивает работу с сессиями внутри проекта
    'django.middleware.common.CommonMiddleware',  #
    'django.middleware.csrf.CsrfViewMiddleware',  # обеспечивает поддержку CSRF-токена
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # обеспечивает корректную авторизацию внутри проекта
    'django.contrib.messages.middleware.MessageMiddleware',  #
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  #
]

ROOT_URLCONF = 'itproger.urls'

""" шаблоны внутри проекта"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'itproger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


""" Список валидаторов, которые используются для проверки надежности паролей пользователей.
 По умолчанию проверка не выполняется и принимаются все пароли. """

# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
