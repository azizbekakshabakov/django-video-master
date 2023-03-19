class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'user_selected' not in context:
            context['user_selected'] = 0
        return context