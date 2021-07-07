"""itproger URL Configuration
отслеживаем различные URL-адреса  """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # из приложения main вызовем файл urls (его создаем) (для этого выше подключаем include)
    path('', include('main.urls'))
]
