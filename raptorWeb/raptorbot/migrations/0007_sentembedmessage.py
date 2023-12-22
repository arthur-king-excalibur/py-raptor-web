# Generated by Django 4.2.7 on 2023-11-25 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0006_discordbotinternal'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmbedMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='gameservers.server')),
                ('message_id', models.CharField(default='', max_length=500)),
                ('sent', models.DateTimeField(auto_now_add=True, verbose_name='Originally Sent')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Sent Embed Message',
                'verbose_name_plural': 'Sent Embed Messages',
            },
        ),
    ]