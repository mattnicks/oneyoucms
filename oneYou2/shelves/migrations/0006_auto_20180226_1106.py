# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-26 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0005_auto_20180225_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelfabstract',
            name='label',
        ),
        migrations.AlterField(
            model_name='shelfabstract',
            name='shelf_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID'),
        ),
    ]
