# Generated by Django 4.2.7 on 2023-11-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0010_sentembedmessage_channel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentembedmessage',
            name='changed_and_unedited',
            field=models.BooleanField(default=False, verbose_name='Changed and Unedited'),
        ),
    ]
