# Generated by Django 4.1 on 2022-08-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_jobdetails_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='logo',
        ),
        migrations.AddField(
            model_name='jobdetails',
            name='Image',
            field=models.ImageField(default='', upload_to='app/img'),
        ),
    ]
