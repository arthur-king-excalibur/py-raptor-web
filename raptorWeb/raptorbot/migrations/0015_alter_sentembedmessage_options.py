# Generated by Django 4.2.7 on 2023-11-26 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0014_alter_discordbottasks_messages_to_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sentembedmessage',
            options={'verbose_name': 'Embed Message', 'verbose_name_plural': 'Embed Messages'},
        ),
    ]
