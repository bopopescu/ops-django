# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-16 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbJobDbBackupHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_instance_id', models.CharField(db_column='db_instance_id', max_length=32)),
                ('dbs', models.TextField(blank=True, db_column='dbs', null=True)),
                ('tables', models.TextField(blank=True, db_column='tables', null=True)),
                ('result', models.TextField(blank=True, db_column='result', null=True)),
                ('dtEventTime', models.DateTimeField(blank=True, db_column='dtEventTime', null=True)),
            ],
            options={
                'db_table': 'db_job_db_backup_history',
            },
        ),
    ]
