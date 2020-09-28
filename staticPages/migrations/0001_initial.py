# Generated by Django 3.1.1 on 2020-09-27 17:27

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Баннер')),
                ('banner_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст на баннер')),
                ('block1', models.CharField(default='Направления деятельности', max_length=255, verbose_name='Заголовок блока1')),
                ('block2', models.CharField(default='Производство', max_length=255, verbose_name='Заголовок блока2')),
                ('block2_text', models.TextField(default='АСПР Групп предоставляет услуги по проектированию и производству следующего электрооборудования:', verbose_name='Тест блока2')),
                ('block3', models.CharField(default='Нам доверяют', max_length=255, verbose_name='Заголовок блока3')),
                ('block4', models.CharField(default='Мы предлагаем своим клиентам', max_length=255, verbose_name='Заголовок блока4')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partner/', verbose_name='Изображение')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staticPages.homepage')),
            ],
            options={
                'verbose_name': 'Элемент блока нам доверяют',
                'verbose_name_plural': 'Элементы блока нам доверяют',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название ')),
                ('name_lower', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staticPages.homepage')),
            ],
            options={
                'verbose_name': 'Элемент блока производство',
                'verbose_name_plural': 'Элементы блока производство',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название ')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание ')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staticPages.homepage')),
            ],
            options={
                'verbose_name': 'Элемент блока мы предлагаем',
                'verbose_name_plural': 'Элементы блока мы предлагаем',
            },
        ),
        migrations.CreateModel(
            name='Block1Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='block1/', verbose_name='Иконка')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название ')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание ')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staticPages.homepage')),
            ],
            options={
                'verbose_name': 'Элемент блока1',
                'verbose_name_plural': 'Элементы блока1',
            },
        ),
    ]