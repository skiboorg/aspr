# Generated by Django 3.1.1 on 2020-11-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_item_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pump_power',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='(Мощность насоса, кВт'),
        ),
    ]
