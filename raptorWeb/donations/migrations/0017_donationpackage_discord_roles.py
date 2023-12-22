# Generated by Django 4.2.7 on 2023-12-18 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0016_donationdiscordrole_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationpackage',
            name='discord_roles',
            field=models.ManyToManyField(blank=True, help_text='A list of created Discord Roles to give when this package is bought.', to='donations.donationdiscordrole', verbose_name='Discord Roles to Give.'),
        ),
    ]