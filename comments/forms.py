from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from upload_files.models import UploadFiles
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    # 在提交评论中用户可以从request获取
    # 内容
    # 文件id 隐藏属性 默认赋值
    # 文件类型 隐藏属性 默认赋值
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'))
    # def __init__(self, *args, **kwargs):
    #     if 'user' in kwargs:
    #         self.user = kwargs.pop("user")
    #     super().__init__(self, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)    
    
    def clean(self):
        # 判断用户登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError("用户尚未登录")
        # 评论对象判断
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data["object_id"]
        try:
            # 获取关联的模型并将其转换为对象
            model_class = ContentType.objects.get(model=content_type)
            # 从模型中得到某一个对象
            # file_obj = UploadFiles.objects.get(pk=object_id)
            self.cleaned_data["model_class"] = model_class
        except ObjectDoesNotExist:
            raise forms.ValidationError("评论对象不存在")
        
        return self.cleaned_data  
    