from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', UsersView.as_view(), name='about'),#
    path('user/<slug:user_slug>/', UserView.as_view(), name='user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('add-video/', AddVideo.as_view(), name='addVideo'),
    path('videos/', Videos.as_view(), name='videos'),
    path('videos/<int:user_id>', UserVideos.as_view(), name='user-videos'),
    path('video/<slug:video_slug>/', VideoView.as_view(), name='video')
]