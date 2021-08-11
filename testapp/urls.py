from django.urls import path, include
from django.contrib import admin
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),

]
