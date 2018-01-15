from django.contrib import admin

# Register your models here.
from .models import UploadedImage

admin.site.register(UploadedImage)
