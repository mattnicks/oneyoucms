# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-07 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0003_release_uuid'),
        ('pages', '0007_auto_20180208_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='oneyou2page',
            name='release',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='release.Release'),
        ),
    ]
