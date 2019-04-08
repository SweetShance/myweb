from django.urls import path
from .views import filesList, showFile

app_name = 'upload_files'
urlpatterns = [
    path('', filesList, name='showfiles' ),
    path('show/<int:pk>', showFile, name="showFile")
]