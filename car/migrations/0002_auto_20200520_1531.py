# Generated by Django 3.0.6 on 2020-05-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='auto',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='countres',
            name='country',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
