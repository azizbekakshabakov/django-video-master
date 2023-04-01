from django.db.models import Count

from .models import *

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.annotate(Count('get_videos'))
        context['users'] = users
        if 'user_selected' not in context:
            context['user_selected'] = 0
        return context