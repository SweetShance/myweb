from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Comments(models.Model):
    content = models.TextField("评论内容", max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(User, verbose_name="评论用户", on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey( ContentType, verbose_name="绑定的对象", on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField("评论对象的id")
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "user:%s id: %s" %(self.auth, self.object_id)

