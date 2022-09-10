from django.contrib import admin
from .models import DocImage

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


admin.site.register(DocImage, BookAdmin)
