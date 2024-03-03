
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('posts', posts, name='posts'),
    path('posts/<pk>', edit, name='edit'),

]
