# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20180208_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oneyou2page',
            name='release',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages', to='release.Release'),
        ),
    ]
