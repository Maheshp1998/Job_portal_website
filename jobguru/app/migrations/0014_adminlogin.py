# Generated by Django 4.1 on 2022-08-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_jobapply_c_ctc_alter_jobapply_e_ctc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
