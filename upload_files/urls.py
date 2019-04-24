from django.urls import path
from .views import filesList, showFile, uploadFiles, download, manage_files, del_file, chick_file, through_file

app_name = 'upload_files'
urlpatterns = [
    path('', filesList, name='showfiles' ),
    path('show/<int:pk>', showFile, name="showFile"),
    path('upload/', uploadFiles, name='upload'),
    path('download/<int:file_pk>', download, name="download"),
    path('manage/', manage_files, name="manage"),
    path('del/<int:file_pk>', del_file, name="delete"),
    path('chick/', chick_file, name="chick"),
    path('through/<int:file_pk>', through_file, name="through")
]