# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-06 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_sitesettings_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='key',
            field=models.CharField(blank=True, help_text='this is used to lookup the site in the api sites endpoint', max_length=255, null=True, unique=True, verbose_name='site key'),
        ),
    ]
