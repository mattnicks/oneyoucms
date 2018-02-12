# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-06 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_advert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_items', wagtail.wagtailcore.fields.StreamField((('menu_item', wagtail.wagtailcore.blocks.CharBlock(classname='menu_item')),))),
            ],
        ),
        migrations.DeleteModel(
            name='Advert',
        ),
    ]