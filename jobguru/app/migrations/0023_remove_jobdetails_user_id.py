# Generated by Django 4.1 on 2022-09-05 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_jobdetails_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='user_id',
        ),
    ]
