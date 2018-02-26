# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-21 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_oneyou2page_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.PHEImage'),
        ),
        migrations.AlterField(
            model_name='header',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.PHEImage'),
        ),
        migrations.AlterField(
            model_name='oneyou2page',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages', to='pages.Theme'),
        ),
    ]