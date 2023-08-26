from django.shortcuts import render
from .models import *
from .mixins import *
from .forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy


def home(request):
    final_users = Final_User.objects.all().order_by('-total')
    return render(request , 'home.html' , {
        'final_users' : final_users
    })



# در کلاس Final_User_Create
class Final_User_Create(CreateView):
    model = Final_User
    form_class = FinalUserForm
    success_url = reverse_lazy("final:home")
    template_name = "user_create.html"

    def form_valid(self, form):
        num_fields = [
            form.cleaned_data['num11'], form.cleaned_data['num12'], form.cleaned_data['num13'],
            form.cleaned_data['num14'], form.cleaned_data['num15'], form.cleaned_data['num16'],
            form.cleaned_data['num17'], form.cleaned_data['num18'], form.cleaned_data['num19'],
            form.cleaned_data['num20'], form.cleaned_data['num21'], form.cleaned_data['num22'],
            form.cleaned_data['num23'], form.cleaned_data['num24']
        ]
        form.instance.total = sum([field for field in num_fields if field is not None])
        return super().form_valid(form)

# در کلاس Final_User_Update
class Final_User_Update(UpdateView, Final_user_FiedsMixin):
    model = Final_User
    form_class = FinalUserForm
    success_url = reverse_lazy("final:home")
    template_name = "user_update.html"

    def form_valid(self, form):
        num_fields = [
            form.cleaned_data['seri1'], form.cleaned_data['seri2'], form.cleaned_data['num11'],
            form.cleaned_data['num12'], form.cleaned_data['num13'], form.cleaned_data['num14'],
            form.cleaned_data['num15'], form.cleaned_data['num16'], form.cleaned_data['num17'],
            form.cleaned_data['num18'], form.cleaned_data['num19'], form.cleaned_data['num20'],
            form.cleaned_data['num21'], form.cleaned_data['num22'], form.cleaned_data['num23'],
            form.cleaned_data['num24']
        ]
        form.instance.total = sum([field for field in num_fields if field is not None])
        return super().form_valid(form)
