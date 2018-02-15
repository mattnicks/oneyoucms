# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-06 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='release',
            name='release_name',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]