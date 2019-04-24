from django.contrib import admin
from .models import FileType, FileLabel, UploadFiles, Associated
from comments.models import Comments
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

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display= ('auth', 'object_id', 'create_time')
    # search_fields = ['object_id', 'auth']

