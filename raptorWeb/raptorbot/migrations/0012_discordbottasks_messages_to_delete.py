# Generated by Django 4.2.7 on 2023-11-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0011_sentembedmessage_changed_and_unedited'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordbottasks',
            name='messages_to_delete',
            field=models.CharField(default='', max_length=16300),
        ),
    ]
