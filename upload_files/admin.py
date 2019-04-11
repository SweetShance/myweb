from django.contrib import admin
from .models import FileType, FileLabel, UploadFiles, Associated
# Register your models here.

admin.site.register(FileType)
admin.site.register(FileLabel)

@admin.register(UploadFiles)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'fileType', 'auth', )
    list_filter = ('title', 'fileType')
    search_fields = ['title']

@admin.register(Associated)
class AssociatedAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_on', 'FileLabel')
    # search_fields = ['file_on', 'FileLabel']
# admin.site.register(Associated)

