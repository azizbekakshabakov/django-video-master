from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied, BadRequest
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

class Videos(DataMixin, ListView):
    model = Video
    template_name = 'mainapp/videos.html'
    context_object_name = 'videos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # def get_queryset(self):
    #     return Video.objects.filter(pk=1)

class UserVideos(DataMixin, ListView):
    model = Video
    template_name = 'mainapp/videos.html'
    context_object_name = 'videos'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(user_selected=context['videos'][0].user_id.pk)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Video.objects.filter(user_id__id=self.kwargs['user_id'])

def index(request):
    return render(request, 'mainapp/index.html')

class UsersView(ListView):
    model = User
    template_name = 'mainapp/about.html'
    context_object_name = 'users'

class UserView(DetailView):
    model = User
    template_name = 'mainapp/user.html'
    slug_url_kwarg = 'user_slug'

def register(request):
    # context_object_name = 'video'
    # pk_url_kwarg = 
    return render(request, 'mainapp/register.html')

def login(request):
    return render(request, 'mainapp/login.html')

class AddVideo(LoginRequiredMixin, CreateView):
    form_class = AddVideoForm
    template_name = 'mainapp/add-video.html'
    successful_url = reverse_lazy('video')
    # login_url = reverse_lazy('home')
    # raise_exception = True

class VideoView(DetailView):
    model = Video
    template_name = 'mainapp/video.html'
    slug_url_kwarg = 'video_slug'
    # context_object_name = 'video'
    # pk_url_kwarg = 



def pageNotFound(request, exception):
    return render(request, 'mainapp/error/page-not-found.html')

def forbidden(request, exception):
    return render(request, 'mainapp/error/forbidden.html')

def badRequest(request, exception):
    return render(request, 'mainapp/error/bad-request.html')

def internalServerError(request):
    return render(request, 'mainapp/error/internal-server-error.html')