from django.urls import path
from .views import save_comment, del_comment

app_name = "comments"
urlpatterns = [
    path('', save_comment, name="save_comment"),
    path('del/<int:com_pk>', del_comment, name="del_comment"),
]