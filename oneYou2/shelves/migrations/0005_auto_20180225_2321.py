# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-25 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('shelves', '0004_promoshelf_button_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppTeaser',
            fields=[
                ('shelfabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shelves.ShelfAbstract')),
                ('heading', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('android_link', models.CharField(max_length=255)),
                ('iphone_line', models.CharField(max_length=255)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            bases=('shelves.shelfabstract',),
        ),
        migrations.CreateModel(
            name='BannerShelf',
            fields=[
                ('shelfabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shelves.ShelfAbstract')),
                ('heading', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('button_text', models.CharField(max_length=255)),
                ('button_link', models.CharField(max_length=255)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            bases=('shelves.shelfabstract',),
        ),
        migrations.AddField(
            model_name='shelfabstract',
            name='shelf_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='label'),
        ),
    ]
