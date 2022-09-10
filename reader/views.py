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
from django.template.response import TemplateResponse
# import urllib library
from urllib.request import urlopen
# import json
import json
from gtts import gTTS
from pygame import mixer

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
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/home', )
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'login.html'

class ViewerView(TemplateView):
    template_name = 'viewer.html'
    word_list = ["Hello", "my", "name", "is", "rishi"]
    extra_context = {'word_list': word_list}


###############################################################################
def get_definition(word):
    api_key = "d98bcc41-7387-4462-97a6-a380a51bbcc6"

    url_part_1 = "https://www.dictionaryapi.com/api/v3/references/learners/json/"
    url_part_2 = word
    url_part_3 = "?key=" + api_key
    final_url = url_part_1 + url_part_2 + url_part_3

    response = urlopen(final_url)

    data_json = json.loads(response.read())
    if len(data_json) == 0:
        print("Error: Word cannot be found")
        return

    all_data = data_json[0]
    #definition_section = all_data['def'][0]['sseq'][0][0][1]['dt'][0]
    definition_section = all_data['meta']['app-shortdef']
    part_of_speech = definition_section['fl']
    definition = definition_section['def']
    print(part_of_speech)
    print(definition)