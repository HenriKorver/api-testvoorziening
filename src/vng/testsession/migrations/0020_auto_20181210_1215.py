# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-10 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0019_auto_20181210_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='tests',
        ),
        migrations.AddField(
            model_name='scenariocase',
            name='scenario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testsession.Scenario'),
        ),
    ]
