# Generated by Django 2.1.3 on 2018-11-13 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0003_auto_20181113_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='type_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testsession.Session_type'),
        ),
    ]
