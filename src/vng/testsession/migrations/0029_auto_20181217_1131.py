# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0028_session_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiontype',
            name='docker_image',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
