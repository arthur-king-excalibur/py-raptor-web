# Generated by Django 3.2.5 on 2022-10-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='server_port',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_address',
            field=models.CharField(default='Default', max_length=50),
        ),
    ]