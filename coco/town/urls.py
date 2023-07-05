from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'town'
urlpatterns = [
    path('townList/', login_required(townList), name='townList'),
    path('newTown/', login_required(newTown), name='newTown'),
    path('createTown/', login_required(createTown), name='createTown'),
    path('setTown/<int:town_id>/', login_required(setTown), name='setTown'),
    path('mainPage/', login_required(mainPage), name='mainPage'),
    path('myTown/', login_required(myTown), name='myTown'),
    path('setting/', login_required(setting), name='setting'),
    path('setting/change_password/', change_password, name='change_password'),
]