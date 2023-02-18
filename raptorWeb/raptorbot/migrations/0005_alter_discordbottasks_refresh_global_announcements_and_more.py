# Generated by Django 4.1.5 on 2023-02-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0004_discordbottasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordbottasks',
            name='refresh_global_announcements',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='discordbottasks',
            name='refresh_server_announcements',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='discordbottasks',
            name='update_members',
            field=models.BooleanField(default=False),
        ),
    ]
