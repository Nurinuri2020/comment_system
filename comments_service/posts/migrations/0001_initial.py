# Generated by Django 3.1.3 on 2020-11-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название поста')),
                ('slug', models.SlugField(max_length=150, verbose_name='Слаг поста')),
                ('body', models.TextField(blank=True, verbose_name='Описание поста')),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')),
            ],
        ),
    ]
