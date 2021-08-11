from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'testapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
