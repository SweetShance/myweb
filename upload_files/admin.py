from django.contrib import admin
from .models import FileType, FileLabel, UploadFiles, Associated
# Register your models here.

admin.site.register(FileType)
admin.site.register(FileLabel)

@admin.register(UploadFiles)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'fileType', 'auth')