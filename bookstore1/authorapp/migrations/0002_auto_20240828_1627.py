# Generated by Django 3.2.19 on 2024-08-28 10:57

import authorapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=authorapp.models.author_image_file_path),
        ),
        migrations.AlterField(
            model_name='author',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
