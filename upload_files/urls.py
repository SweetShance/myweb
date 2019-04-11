from django.urls import path
from .views import filesList, showFile, uploadFiles

app_name = 'upload_files'
urlpatterns = [
    path('', filesList, name='showfiles' ),
    path('show/<int:pk>', showFile, name="showFile"),
    path('upload/', uploadFiles, name='upload'),
]