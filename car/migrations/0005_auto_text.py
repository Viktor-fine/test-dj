# Generated by Django 3.0.6 on 2020-07-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20200718_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='text',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
