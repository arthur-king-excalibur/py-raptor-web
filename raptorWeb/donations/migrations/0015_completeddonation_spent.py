# Generated by Django 4.2.7 on 2023-12-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0014_alter_donationpackage_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeddonation',
            name='spent',
            field=models.IntegerField(default=0, help_text='The amount spent for this donation.', verbose_name='Amount Spent'),
        ),
    ]
