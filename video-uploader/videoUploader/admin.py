from django.contrib import admin
from .models import upload_video

# Register your models here.
# class VideoAdmin(admin.ModelAdmin):
#   list_display = ('id')

admin.site.register(upload_video)