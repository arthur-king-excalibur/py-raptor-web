# Generated by Django 4.2.7 on 2023-12-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameservers', '0010_alter_server_modpack_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='rcon_address',
            field=models.CharField(default='', help_text='The IP address used to send RCON commands to this server.', max_length=200, verbose_name='RCON Connection Address'),
        ),
        migrations.AddField(
            model_name='server',
            name='rcon_password',
            field=models.CharField(default='', help_text='The password used to authenticate when sending RCON commands to this server.', max_length=500, verbose_name='RCON Connection Password'),
        ),
        migrations.AddField(
            model_name='server',
            name='rcon_port',
            field=models.IntegerField(default=0, help_text='The network port used to send RCON commands to this server.', verbose_name='RCON Connection Port'),
        ),
    ]
