# Generated by Django 4.2.7 on 2023-12-18 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0017_donationpackage_discord_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeddonation',
            name='gave_roles_count',
            field=models.IntegerField(default=0, help_text='The amount of times Discor roles were given for this donation.', verbose_name='Times Discord roles were given'),
        ),
    ]
