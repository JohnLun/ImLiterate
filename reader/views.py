from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'reader/register.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('', )
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'reader/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'reader/login.html'
