# Generated by Django 3.1.1 on 2020-11-03 11:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20201103_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='full_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание'),
        ),
    ]
