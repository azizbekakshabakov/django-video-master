from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),#
    path('user/<slug:user_slug>/', user, name='user'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add-video/', AddVideo.as_view(), name='addVideo'),
    path('videos/', Videos.as_view(), name='videos'),
    path('videos/<int:user_id>', UserVideos.as_view(), name='user-videos'),
    path('video/<slug:video_slug>/', Video.as_view(), name='video')
]