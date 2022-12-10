# Generated by Django 4.1 on 2022-08-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobapply_delete_jobapplypage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapply',
            old_name='additional_info',
            new_name='addinfo1',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='college',
            new_name='c_city1',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='company_name',
            new_name='c_city2',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='dae_to',
            new_name='c_city3',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='current_salary',
            new_name='c_ctc',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='date_from',
            new_name='college1',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='datefrom',
            new_name='college2',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='dateto',
            new_name='college3',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='degree',
            new_name='companyname1',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='job_title',
            new_name='companyname2',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='qualification',
            new_name='companyname3',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='currently_work_here',
            new_name='cwh1',
        ),
        migrations.RenameField(
            model_name='jobapply',
            old_name='expected_salary',
            new_name='e_ctc',
        ),
        migrations.AddField(
            model_name='jobapply',
            name='addinfo2',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='addinfo3',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='cwh2',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='cwh3',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='date_from1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='date_from2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='date_from3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='date_to1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='date_to2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='date_to3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='datefrom1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='datefrom2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='datefrom3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='dateto1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='dateto2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='dateto3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='degree1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='degree2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='degree3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='jobposiion1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='jobposiion2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='jobposiion3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='qualification1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='qualification2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapply',
            name='qualification3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
