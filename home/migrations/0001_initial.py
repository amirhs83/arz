# Generated by Django 5.0.4 on 2024-09-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('on', models.CharField(choices=[('1', 'فارکس کلاب'), ('2', 'فیوچرز کلاب'), ('3', 'اسپات کلاب')], default='فارکس کلاب', max_length=20)),
            ],
        ),
    ]
