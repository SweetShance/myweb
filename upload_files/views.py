from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import UploadFiles, FileType, FileLabel, Associated
from filesManage.views import login_utils
from .forms import UploadForms
from django.utils import timezone

# Create your views here.
def filesList(request):
    request_get = request.GET.get("a")
    # 从request接收的有两个单引号
    file_type = FileType.objects.get(fileType=request_get)
    files_all = UploadFiles.objects.filter(fileType=file_type.pk)
    template_name = 'upload_files/show_files_about_type.html'
    context = login_utils(request)
    context["files_all"] = files_all
    return render(request, template_name=template_name, context=context)
    # response = render(request, template_name=template_name, context=context)

def showFile(request, pk):
    file =  get_object_or_404(UploadFiles, pk=pk)
    context = login_utils(request)
    context['file'] = file
    return render(request, 'upload_files/show_content.html', context=context)

def uploadFiles(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == "POST":
            uploadForms = UploadForms(request.POST, request.FILES, user=request.user)
            if uploadForms.is_valid(): 
                uploadfiles = UploadFiles()
                uploadfiles.title = uploadForms.cleaned_data["title"]
                uploadfiles.introduction = uploadForms.cleaned_data["introduction"]
                uploadfiles.fileType = uploadForms.cleaned_data["fileType"]
                uploadfiles.auth = uploadForms.cleaned_data["user"]
                uploadfiles.content = uploadForms.cleaned_data["content"]
                # # uploadfiles.fileLabel.set(uploadForms.cleaned_data["fileLabel"])
                uploadfiles.icon = uploadForms.cleaned_data["icon"]
                uploadfiles.save()    
                # 创建多对多关系
                # get_object_or_404(UploadFiles, pk=uploadfiles.pk)
                for i in uploadForms.cleaned_data["fileLabel"]:
                    Associated.objects.create(FileLabel=get_object_or_404(FileLabel, fileLabel=i), file_on=uploadfiles)
                context["resoult"] = "保存成功"
        else:
            uploadForms = UploadForms()
        context["uploadForms"] = uploadForms
    
        return render(request, template_name="upload_files/upload_file.html", context=context)
    else:
        return redirect(reverse('index'))