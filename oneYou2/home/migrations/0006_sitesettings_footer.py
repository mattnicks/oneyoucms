# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-13 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20180212_1252'),
        ('home', '0005_sitesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='footer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.Footer'),
        ),
    ]
