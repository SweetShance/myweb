# Generated by Django 2.1 on 2019-04-02 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfiles',
            name='create_date',
        ),
    ]
