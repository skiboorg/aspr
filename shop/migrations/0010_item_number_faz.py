# Generated by Django 3.1.1 on 2020-11-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20201103_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='number_faz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Параметр: Количество фаз'),
        ),
    ]
