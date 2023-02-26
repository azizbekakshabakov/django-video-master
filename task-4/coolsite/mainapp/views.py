from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied, BadRequest

from .models import *

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'mainapp/about.html', context=context)

def user(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'user': user
    }
    return render(request, 'mainapp/user.html', context=context)

def register(request):
    return render(request, 'mainapp/register.html')

def login(request):
    return render(request, 'mainapp/login.html')

def addVideo(request):
    return render(request, 'mainapp/add-video.html')

def videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'mainapp/videos.html', context=context)


def pageNotFound(request, exception):
    return render(request, 'mainapp/error/page-not-found.html')

def forbidden(request, exception):
    return render(request, 'mainapp/error/forbidden.html')

def badRequest(request, exception):
    return render(request, 'mainapp/error/bad-request.html')

def internalServerError(request):
    return render(request, 'mainapp/error/internal-server-error.html')