# Generated by Django 4.1 on 2022-09-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_profile_pic_candidate_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='objective',
            field=models.TextField(max_length=1000),
        ),
    ]
