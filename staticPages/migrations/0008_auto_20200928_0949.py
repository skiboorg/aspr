# Generated by Django 3.1.1 on 2020-09-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticPages', '0007_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='page_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание страницы (Тег Description)'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='page_title',
            field=models.CharField(default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация', max_length=255, verbose_name='Заголовок страницы (Тег Titlе)'),
        ),
        migrations.AddField(
            model_name='avtomatizaciyapage',
            name='page_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание страницы (Тег Description)'),
        ),
        migrations.AddField(
            model_name='avtomatizaciyapage',
            name='page_title',
            field=models.CharField(default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация', max_length=255, verbose_name='Заголовок страницы (Тег Titlе)'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание страницы (Тег Description)'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_title',
            field=models.CharField(default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация', max_length=255, verbose_name='Заголовок страницы (Тег Titlе)'),
        ),
        migrations.AddField(
            model_name='proizvodsvopage',
            name='page_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание страницы (Тег Description)'),
        ),
        migrations.AddField(
            model_name='proizvodsvopage',
            name='page_title',
            field=models.CharField(default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация', max_length=255, verbose_name='Заголовок страницы (Тег Titlе)'),
        ),
        migrations.AddField(
            model_name='worktypepage',
            name='page_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание страницы (Тег Description)'),
        ),
        migrations.AddField(
            model_name='worktypepage',
            name='page_title',
            field=models.CharField(default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация', max_length=255, verbose_name='Заголовок страницы (Тег Titlе)'),
        ),
        migrations.AlterField(
            model_name='worktypepage',
            name='title',
            field=models.CharField(default='Направления компании', max_length=255, verbose_name='заголовок (H1)'),
        ),
    ]
