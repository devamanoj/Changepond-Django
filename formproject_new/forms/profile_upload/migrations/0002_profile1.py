# Generated by Django 4.2.15 on 2024-08-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
