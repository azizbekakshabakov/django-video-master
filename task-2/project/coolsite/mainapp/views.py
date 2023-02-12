from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied, BadRequest

def index(request):
    return HttpResponse('''
        <!DOCTYPE html>
        <html>

        <head>
        <title>Video Master</title>
        </head>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

        <body>

        <nav class="navbar navbar-expand-lg bg-dark bg-body-tertiary" data-bs-theme="dark">
            <div class="container">
                <a class="navbar-brand" href="#">Video Master</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Recommendations</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Add video</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Write comment</a>
                        </li>
                    </ul>
                    <ul class="navbar-nav mb-2 mb-lg-0 d-flex">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Sign in</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <h1 class="text-center mt-5 pt-5">Welcome to the video hosting site</h1> 

        </body>

        </html>
    ''')

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