# Generated by Django 3.2.5 on 2022-08-22 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0013_userprofileinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name': 'User - Extra Information', 'verbose_name_plural': 'Users - Extra Information'},
        ),
    ]