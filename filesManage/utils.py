from upload_files.models import UploadFiles, FileType, FileLabel

def statistical(request):
    # 各种文件的个数
    context = {}
    fielTypes = FileType.objects.all()
    for fileType in fielTypes:
        file_count_about_type = UploadFiles.objects.filter(fileType=fileType.pk).count()
        context[fileType.fileType] = file_count_about_type
    return context