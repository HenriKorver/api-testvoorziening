# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0023_auto_20181211_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('test_file', models.FileField(upload_to='', verbose_name='/files/uploaded_files')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='test_result',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='/files/log'),
        ),
        migrations.AddField(
            model_name='session',
            name='test',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsession.TestSession'),
        ),
    ]
