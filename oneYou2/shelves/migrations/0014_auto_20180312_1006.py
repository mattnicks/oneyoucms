# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-12 10:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0013_auto_20180306_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appteaser',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bannershelf',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
    ]
