from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
# from .forms import DocumentForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

# class UploadView(TemplateView):
#     template_name = 'upload.html'

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'upload.html', {
#         'form':form
#     })

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/home'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('', )
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'login.html'
