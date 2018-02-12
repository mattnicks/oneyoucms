# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-07 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('pages', '0005_auto_20180207_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('menu_items', wagtail.wagtailcore.fields.StreamField((('simple_menu_item', wagtail.wagtailcore.blocks.StructBlock((('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(label='External link', required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))))),))),
                ('follow_us', wagtail.wagtailcore.fields.StreamField((('social_media_link', wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[])), ('link', wagtail.wagtailcore.blocks.URLBlock(label='External link', required=False))))),))),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]