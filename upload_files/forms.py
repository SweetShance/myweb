from django import forms
from django.forms import widgets 
from .models import FileType, FileLabel

FILETYPE = FileType.objects.all()

class UploadForms(forms.Form):
    # 将标签添加到迭代器中
    FAVORITE_COLORS_CHOICES = ((i,i) for i in FileLabel.objects.all())
    # FAVORITE_COLORS_CHOICES = FileLabel.objects.all()
    title = forms.CharField(label="标题",max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    introduction = forms.CharField(label="简介", max_length=500, widget=forms.Textarea(attrs={"class": "form-control", "id": "exampleFormControlSelect2"}))
    # auth = form
    
    fileType = forms.ModelChoiceField(queryset=FILETYPE, empty_label="请选择", widget=forms.Select(attrs={"class": "form-control form-control-lg"}))
    fileLabel = forms.MultipleChoiceField(label="标签", widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    # fileLabel = forms.ModelChoiceField(queryset=FAVORITE_COLORS_CHOICES, empty_label="请选择", widget=forms.Select(attrs={"class": "form-control form-control-lg"}))
    content = forms.FileField(label="文件", widget=forms.ClearableFileInput(attrs={"class": "form-control", 'title': '图片'}))
    icon = forms.ImageField(label="封面")
    icon.widget.attrs.update({'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(UploadForms, self).__init__(*args, **kwargs)
        
        # self.clean()
    def clean(self):
        
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
            
        else:
            raise forms.ValidationError("尚未登录")
        
        title = self.cleaned_data["title"]
        introduction = self.cleaned_data["introduction"]
        fileType = self.cleaned_data["fileType"]
        label = self.cleaned_data["fileLabel"]
        content = self.cleaned_data["content"]
        icon = self.cleaned_data["icon"]

        return self.cleaned_data

