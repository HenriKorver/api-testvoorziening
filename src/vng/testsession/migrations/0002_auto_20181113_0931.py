# Generated by Django 2.1.3 on 2018-11-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='API_endpoint',
            new_name='api_endpoint',
        ),
        migrations.AlterField(
            model_name='session',
            name='stopped',
            field=models.DateTimeField(null=True),
        ),
    ]
