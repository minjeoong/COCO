from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'user'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('new_profile/', login_required(new_profile), name='new_profile'),
    path('create_profile/', login_required(create_profile), name='create_profile'),
]