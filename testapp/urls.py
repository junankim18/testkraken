from django.urls import path, include
from django.contrib import admin
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('find/', find, name = "find"), 
    path('accept/<int:pk>', accept, name = "accept"), 
    path('reject/<int:pk>', reject, name = "reject"), 
    path('mypage/', mypage, name = "mypage"), 
    path('follow/<int:pk>', follow, name = "follow"), 
    path('find_card', find_card, name="find_card"),
    path('get/<int:pk>', get, name="get"),
    path('page/<int:my_id>/<int:other_id>', page, name = "page"),
    path('trade/<int:pk>', trade, name = "trade"),
    path('tradepage/', tradepage, name = "tradepage"),
   # 나의 id와 상대방의 id를 동시에 전달함 

]
