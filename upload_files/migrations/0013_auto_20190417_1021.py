# Generated by Django 2.1 on 2019-04-17 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_files', '0012_auto_20190411_0137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfiles',
            options={'ordering': ['-create_time']},
        ),
    ]
