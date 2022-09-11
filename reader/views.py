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
import glob
import os
#word_list = []

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

def detect_text(request):
    """Detects text in the file."""
    print("hi")
    list_of_files = glob.glob('./media/*') # * means all if need specific format then *.csv
    if len(list_of_files) > 0:
        path = max(list_of_files, key=os.path.getctime)

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./static/CREDS/striped-option-362104-9d3f8028bfa8.json"
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    res = []
    for i in range(1,len(texts)):
        #print(texts[i].description)
        res.append(texts[i].description)

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    image_file.close()
    os.remove(path)
    print(path)

    word_list = res
    extra_context = {'word_list': word_list}
    return render(request, 'viewer.html', extra_context)

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

    #extra_context = {'word_list': word_list}
