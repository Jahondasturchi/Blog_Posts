from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('update/', update, name='update'),
]
