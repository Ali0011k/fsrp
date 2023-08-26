from django.http import HttpResponseForbidden 


class Final_user_FiedsMixin():
    def dispatch(self, request, *args, **kwargs):
        self. fields = '__all__'
        return super().dispatch(request, *args, **kwargs)