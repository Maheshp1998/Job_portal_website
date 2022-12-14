# Generated by Django 4.1 on 2022-08-22 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_jobdetails_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=250)),
                ('firstname', models.CharField(max_length=200)),
                ('middlename', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('marital_staus', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('linkden', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('qualification', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('date_from', models.CharField(max_length=200)),
                ('dae_to', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('currently_work_here', models.CharField(max_length=20)),
                ('datefrom', models.CharField(max_length=200)),
                ('dateto', models.CharField(max_length=200)),
                ('additional_info', models.TextField(max_length=5000)),
                ('skills', models.TextField(max_length=1000)),
                ('resume', models.FileField(upload_to='app/candidate/resume')),
                ('current_salary', models.BigIntegerField()),
                ('expected_salary', models.BigIntegerField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
            ],
        ),
    ]
