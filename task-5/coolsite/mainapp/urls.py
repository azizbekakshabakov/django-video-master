from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),#
    path('user/<slug:user_slug>/', user, name='user'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add-video/', addVideo, name='addVideo'),
    path('videos/', videos, name='videos'),
    path('videos/<int:user_id>', userVideos, name='user-videos'),
    path('video/<slug:video_slug>/', video, name='video')
]