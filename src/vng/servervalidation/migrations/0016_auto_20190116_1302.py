# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-16 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0015_auto_20190116_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='jwt',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]
