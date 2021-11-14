# Generated by Django 3.2.9 on 2021-11-14 16:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20211112_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'страница',
                'verbose_name_plural': 'страницы',
            },
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('keywords', models.CharField(max_length=100, verbose_name='keywords')),
                ('description', models.TextField(verbose_name='description')),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
            ],
            options={
                'verbose_name': 'SEO блок',
                'verbose_name_plural': 'SEO блок',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_picture', models.ImageField(upload_to='cms_pages/', verbose_name='главная картинка')),
                ('additional_picture', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='cms_pages/', verbose_name='галерея картинок'), size=5)),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
            ],
        ),
    ]
