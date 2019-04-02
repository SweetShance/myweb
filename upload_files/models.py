from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class FileType(models.Model):
    fileType = models.CharField(max_length=20)

    def __str__(self):
        return self.fileType


class FileLabel(models.Model):
    fileLabel = models.CharField(max_length=20, primary_key=True)
    
    def __str__(self):
        return self.fileLabel


class UploadFiles(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField(max_length=500) #简介
    fileType = models.ForeignKey(FileType, on_delete=models.DO_NOTHING)
    auth = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.FileField(upload_to='files') # 内容
    fileLabel = models.ManyToManyField(FileLabel, through='Associated')
    create_time = models.DateField(default=timezone.now)
    
    def __str__(self):
        return "<id: %s name: %s>" %(self.pk, self.title)


class Associated(models.Model):
    FileLabel = models.ForeignKey(FileLabel, on_delete=models.CASCADE)
    file_on = models.ForeignKey(UploadFiles, on_delete=models.CASCADE) 
