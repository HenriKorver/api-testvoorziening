# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0028_auto_20190122_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmantestresult',
            name='log_json',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='/files/log'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
        migrations.AlterField(
            model_name='postmantestresult',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]