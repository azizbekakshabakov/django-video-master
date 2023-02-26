from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),#
    path('user/<int:user_id>/', user, name='user'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add-video/', addVideo, name='addVideo'),
    path('videos/', videos, name='videos')
]