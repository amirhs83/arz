# Generated by Django 5.0.4 on 2024-09-11 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_weblog_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='uploads/images')),
                ('video', models.FileField(null=True, upload_to='uploads/videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='weblog',
            name='img',
            field=models.ImageField(null=True, upload_to='uploads/images'),
        ),
    ]
