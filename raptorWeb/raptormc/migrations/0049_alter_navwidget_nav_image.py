# Generated by Django 4.2.7 on 2023-11-18 23:48

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0048_alter_navwidget_nav_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navwidget',
            name='nav_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', help_text='The image used as an identifier/name for this Nav Widget. Optimal size for this image is w250xh72 or within the same aspect ratio.', keep_meta=True, quality=100, scale=None, size=[250, 72], upload_to='navwidgetimage', verbose_name='Nav Widget Image'),
        ),
    ]
