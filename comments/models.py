from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Comments(models.Model):
    content = models.TextField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    file_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    file_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "user:%s id: %s" %(self.auth, self.file_id)

