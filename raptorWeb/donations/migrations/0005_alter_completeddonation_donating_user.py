# Generated by Django 4.2.7 on 2023-12-10 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0004_alter_donationpackage_commands_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeddonation',
            name='donating_user',
            field=models.ForeignKey(blank=True, help_text='The user who donated. This will be blank if the donator was not logged in at the time of donation.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Donating User'),
        ),
    ]
