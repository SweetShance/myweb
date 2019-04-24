from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import ObjectDoesNotExist
from .forms import CommentForm
from .models import Comments
# Create your views here.

def save_comment(request):
    url_form = request.META.get("HTTP_REFERER", reverse("index"))
    if request.method == "POST":
        com_form = CommentForm(request.POST, user=request.user)
        if com_form.is_valid():
            # 保存数据
            content = com_form.cleaned_data['content']
            auth = com_form.cleaned_data['user']
            content_type = com_form.cleaned_data['model_class']
            object_id = com_form.cleaned_data['object_id']
            Comments.objects.create(content=content, auth=auth, content_type=content_type, object_id=object_id)
            return redirect(url_form)
    return render(request, 'index')


def del_comment(request, com_pk):
    url_form = request.META.get("HTTP_REFERER", reverse("index"))    
    com_obj = get_object_or_404(Comments, pk=com_pk)
    com_obj.delete()
    return redirect(url_form)