from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from .models import UploadFiles, FileType, FileLabel, Associated
from filesManage.views import login_utils
from .forms import UploadForms

# Create your views here.
def pageList(request):
    context = {}
    request_get = request.GET.get("a")
    page_num = request.GET.get('page', 1) # 获取页码参数页码请求
    # 从request接收的有两个单引号
    file_type = FileType.objects.get(fileType=request_get)
    files_all = UploadFiles.objects.filter(fileType=file_type.pk)
    paginator = Paginator(files_all, 15)

    # page = request.GET.get('page')
    page_of_files = paginator.get_page(page_num) # 获取页面
    context['a'] = request_get
    context["pages"] = paginator.page_range
    context["page_of_files"] = page_of_files
    return context


def filesList(request):
    # request_get = request.GET.get("a")
    # # 从request接收的有两个单引号
    # file_type = FileType.objects.get(fileType=request_get)
    # files_all = UploadFiles.objects.filter(fileType=file_type.pk)
    
    template_name = 'upload_files/show_files_about_type.html'
    context = login_utils(request)
    # context["files_all"] = files_all
    context = pageList(request)
    return render(request, template_name=template_name, context=context)
    # response = render(request, template_name=template_name, context=context)

def showFile(request, pk):
    file =  get_object_or_404(UploadFiles, pk=pk)
    context = login_utils(request)
    context['file'] = file
    print(str(file.fileType) == "文件")
    context['type'] = str(file.fileType) == "视频"
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