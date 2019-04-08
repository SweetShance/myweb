from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UploadFiles, FileType

# Create your views here.
def filesList(request):
    request_get = request.GET.get("a")
    # 从request接收的有两个单引号
    file_type = FileType.objects.get(fileType=request_get)
    files_all = UploadFiles.objects.filter(fileType=file_type.pk)
    template_name = 'upload_files/show_files_about_type.html'
    context = {
        "files_all": files_all,
        "file_type": file_type,
    }
    return render(request, template_name=template_name, context=context)

def showFile(request, pk):
    file =  get_object_or_404(UploadFiles, pk=pk)
    context = {
        'file': file
    }    
    return render(request, 'upload_files/show_content.html', context=context)