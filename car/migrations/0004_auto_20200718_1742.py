# Generated by Django 3.0.6 on 2020-07-18 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20200520_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'verbose_name_plural': 'Название марки'},
        ),
        migrations.AlterModelOptions(
            name='countres',
            options={'verbose_name_plural': 'Страна производитель'},
        ),
    ]
