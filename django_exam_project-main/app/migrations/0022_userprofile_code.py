# Generated by Django 5.0.6 on 2024-09-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_userprofile_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]
