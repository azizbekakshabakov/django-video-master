from django import template
from mainapp.models import *

register = template.Library()

@register.simple_tag()
def get_users(filter=None):
    if not filter:
        return User.objects.all()
    else:
        return User.objects.filter(pk=filter)

@register.inclusion_tag('mainapp/tags/list_users.html')
def show_users(sort=None):
    if not sort:
        users = User.objects.all()
    else:
        users = User.objects.order_by(sort)

    return {"users": users}

@register.inclusion_tag('mainapp/tags/list_users_videos.html')
def show_users_videos(sort=None, user_selected=0):
    if not sort:
        users = User.objects.all()
    else:
        users = User.objects.order_by(sort)

    return {"users": users, 'user_selected': user_selected}

@register.inclusion_tag('mainapp/tags/list_videos.html')
def show_videos(user_selected=0):
    if user_selected == 0:
        videos = Video.objects.all()
    else:
        videos = Video.objects.filter(user_id=user_selected)

    return {"videos": videos}