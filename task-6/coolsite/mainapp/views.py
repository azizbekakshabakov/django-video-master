from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied, BadRequest
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import *
from .models import *

class Videos(ListView):
    model = Video
    template_name = 'mainapp/videos.html'
    # context_object_name = 'videos'
    # extra_context = {
    #     'user_selected': 0
    # }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_selected'] = 0
        return context

    # def get_queryset(self):
    #     return Video.objects.filter(pk=1)

class UserVideos(ListView):
    model = Video
    template_name = 'mainapp/videos.html'
    # context_object_name = 'videos'
    allow_empty = False
    # extra_context = {
    #     'user_selected': 0
    # }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_selected'] = self.kwargs['user_id']
        return context

    def get_queryset(self):
        return Video.objects.filter(user_id__id=self.kwargs['user_id'])

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

class AddVideo(CreateView):
    form_class = AddVideoForm
    template_name = 'mainapp/add-video.html'
    successful_url = reverse_lazy('video')

def addVideo(request):
    if request.method == 'POST':
        form = AddVideoForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('videos')
    else:
        form = AddVideoForm

    return render(request, 'mainapp/add-video.html', {'form': form})

class Video(DetailView):
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