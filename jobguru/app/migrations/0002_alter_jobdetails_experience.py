# Generated by Django 4.1 on 2022-08-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='experience',
            field=models.CharField(default='', max_length=50),
        ),
    ]
