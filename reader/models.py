# from django.db import models

# # Create your models here.
# class Document(models.Model):
#     descriptoin = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class DocImage(models.Model):
    name = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='imLiterate/media')

