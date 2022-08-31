# Generated by Django 3.2.5 on 2022-08-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0022_alter_serverinformation_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverinformation',
            name='description',
        ),
        migrations.AddField(
            model_name='serverinformation',
            name='modpack_description',
            field=models.TextField(default='Modpack Description', max_length=1500, verbose_name='Modpack Description'),
        ),
        migrations.AddField(
            model_name='serverinformation',
            name='server_description',
            field=models.TextField(default='Server Description', max_length=1500, verbose_name='Server Description'),
        ),
    ]