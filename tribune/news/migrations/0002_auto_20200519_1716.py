# Generated by Django 3.0.6 on 2020-05-19 14:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo'),
        ),
    ]
