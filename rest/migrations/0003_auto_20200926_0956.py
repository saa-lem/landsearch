# Generated by Django 3.1.1 on 2020-09-26 09:56

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20200926_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]