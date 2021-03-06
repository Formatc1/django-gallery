# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django_gallery.models.gallery
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(editable=False, max_length=250, unique=True, verbose_name='title slug'),
        ),
        migrations.AlterField(
            model_name='image',
            name='large_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to=django_gallery.models.gallery.get_storage_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to=django_gallery.models.gallery.get_storage_path),
        ),
    ]
