from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from django.urls import reverse
from django.utils import timezone, http
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType

import os
from .models import UploadFiles, FileType, FileLabel, Associated
from filesManage.views import login_utils
from .forms import UploadForms
from comments.forms import CommentForm
from comments.models import Comments

# Create your views here.
def pageList(request):
    context = {}
    request_get = request.GET.get("a")
    page_num = request.GET.get('page', 1) # 获取页码参数页码请求
    # 从request接收的有两个单引号
    file_type = FileType.objects.get(fileType=request_get)
    files_all = UploadFiles.objects.filter(fileType=file_type.pk, is_active=1)
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
    context_L = pageList(request)
    for k, v in context_L.items():
        context[k] = v
    return render(request, template_name=template_name, context=context)
    # response = render(request, template_name=template_name, context=context)

def showFile(request, pk):
    file =  get_object_or_404(UploadFiles, pk=pk)
    context = login_utils(request)
    context['file'] = file
    context['type'] = str(file.fileType) == "视频"
    # 关联文件的
    content_type = ContentType.objects.get_for_model(file)
    # 评论 初始化隐藏标签的内容 一个是文件类型 二是id
    data = {}
    data["content_type"] = content_type.model
    data["object_id"] = pk
    commentForm = CommentForm(initial=data)

    # 提交评论表单
    context["commentForm"] = commentForm
    # 评论内容
    context["comments"] = Comments.objects.filter(object_id=pk)
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


def download(request, file_pk):
    # 打开文件

    file_obj = get_object_or_404(UploadFiles, pk=file_pk)
    file_name = str(file_obj.content).split("/")[1]
    print(file_name)
    file_open = open(os.path.join("media", str(file_obj.content)), 'rb')
    response = FileResponse(file_open)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{0}"'.format(http.urlquote(file_name) )
    return response


def manage_files(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            files = UploadFiles.objects.all()
        else:
            files = UploadFiles.objects.filter(auth=request.user)
        context = {
            "files": files
        }
        return render(request, 'upload_files/manage_base.html', context=context)
    return redirect(reverse('index'))
def del_file(request, file_pk):
    if request.user.is_authenticated:
        url_form = request.META.get("HTTP_REFERER", reverse("index"))
        file = get_object_or_404(UploadFiles, pk=file_pk)
        file.delete()
        return redirect(url_form)
    return redirect(reverse('index'))


def chick_file(request):
    if request.user.is_superuser:
        files = UploadFiles.objects.filter(is_active=0)
        context = {
            "files": files
        }
        return render(request, "upload_files/chick_file.html", context)
    else:
        return redirect('index')

def through_file(request, file_pk):
    com_form = request.META.get("HTTP_REFERER", reverse('index'))
    if request.user.is_superuser:
        file = get_object_or_404(UploadFiles, pk=file_pk)
        file.is_active = 1
        file.save()
        return redirect(com_form)
    else:
        return redirect('index')