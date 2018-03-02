# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-27 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0007_auto_20180226_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appshelf',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.PHEImage'),
        ),
        migrations.AlterField(
            model_name='bannershelf',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.PHEImage'),
        ),
    ]
