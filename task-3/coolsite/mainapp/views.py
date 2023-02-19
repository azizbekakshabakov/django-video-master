from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied, BadRequest

from .models import *

def index(request):
    return render(request, 'mainapp/index.html', {'title': 'Video Master'})

def about(request):
    users = User.objects.all()
    return render(request, 'mainapp/about.html', {'title': 'Video Master', 'users': users})

# def 

# МОЖНО ВЫЗВАТЬ 403, ЕСЛИ ВВЕСТИ НЕВЕРНЫЙ ЕМАИЛ
def moderator(request):
    if request.GET['email'] != 'moderator@gmail.com':
        raise PermissionDenied()

    return HttpResponse(f"<h1>Ваш ник: {request.GET['email']}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 (Not Found) - Страница не найдена</h1>')

def forbidden(request, exception):
    return HttpResponseForbidden('<h1>403 (Forbidden) - У вас нет прав на просмотр этой страницы</h1>')

def badRequest(request, exception):
    return HttpResponseBadRequest('<h1>400 (Bad Request) - сервер не может или не будет обрабатывать запрос</h1>')

def internalServerError(request):
    return HttpResponseServerError('<h1>500 (Internal Server Error) - внутренняя ошибка сервера</h1>')