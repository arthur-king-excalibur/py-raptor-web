# Generated by Django 4.1.5 on 2023-02-16 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameservers', '0002_alter_serverstatistic_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='archived',
            field=models.BooleanField(default=False, help_text='If a server is archived, it will not be displayed on the website or queried. Use this instead of deleting servers.', verbose_name='Archived'),
        ),
    ]
