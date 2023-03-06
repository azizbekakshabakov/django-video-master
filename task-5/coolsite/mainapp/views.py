from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied, BadRequest

from .forms import *
from .models import *

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def user(request, user_slug):
    user = get_object_or_404(User, slug=user_slug)
    context = {
        'user': user
    }
    return render(request, 'mainapp/user.html', context=context)

def register(request):
    return render(request, 'mainapp/register.html')

def login(request):
    return render(request, 'mainapp/login.html')

def addVideo(request):
    if request.method == 'POST':
        form = AddVideoForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Video.objects.create(**form.cleaned_data)
                return redirect('videos')
            except:
                form.add_error(None, 'Error adding')
    else:
        form = AddVideoForm

    return render(request, 'mainapp/add-video.html', {'form': form})

def videos(request):
    context = {
        'user_selected': 0
    }
    return render(request, 'mainapp/videos.html', context=context)

def userVideos(request, user_id):
    context = {
        'user_selected': user_id
    }
    return render(request, 'mainapp/videos.html', context=context)

def video(request, video_slug):
    video = get_object_or_404(Video, slug=video_slug)

    context = {
        'video': video
    }

    return render(request, 'mainapp/video.html', context=context)



def pageNotFound(request, exception):
    return render(request, 'mainapp/error/page-not-found.html')

def forbidden(request, exception):
    return render(request, 'mainapp/error/forbidden.html')

def badRequest(request, exception):
    return render(request, 'mainapp/error/bad-request.html')

def internalServerError(request):
    return render(request, 'mainapp/error/internal-server-error.html')