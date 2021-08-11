from django.urls import path, include
from django.contrib import admin

app_name = 'testapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls'))
]
