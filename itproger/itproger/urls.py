"""itproger URL Configuration
отслеживаем различные URL-адреса  """
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # из приложения main вызовем файл urls (его создаем) (для этого выше подключаем include)
    path('', include('main.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
