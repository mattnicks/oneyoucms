# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-26 11:06
from __future__ import unicode_literals

from django.db import migrations
import shelves.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20180225_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oneyou2page',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('section_heading', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(help_text='Not displayed in the front end', label='ID', required=False))), classname='full title', icon='title')), ('backwards_compatible_content', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('body', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(label='ID', required=False))), icon='folder-inverse', label='Previous content')), ('find_out_more_dropdown', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('links', wagtail.wagtailcore.blocks.StreamBlock((('simple_menu_item', wagtail.wagtailcore.blocks.StructBlock((('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(label='External link', required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))))),), icon='arrow-left', label='Items')), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(label='ID', required=False))), icon='order-down', label='Link dropdown')), ('video', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subheading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('body', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('video', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(label='ID', required=False))), icon='media')), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('items', wagtail.wagtailcore.blocks.StreamBlock((('backwards_compatible_content', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('body', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(label='ID', required=False))), icon='folder-inverse', label='Previous content')), ('video', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subheading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('body', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('video', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(label='ID', required=False))), icon='media'))), icon='arrow-left', label='Items')), ('shelf_id', wagtail.wagtailcore.blocks.CharBlock(label='ID', required=False))), icon='repeat')), ('promoshelf', shelves.blocks.PromoShelfChooserBlock(icon='image', target_model='shelves.PromoShelf')), ('bannershelf', shelves.blocks.BannerShelfChooserBlock(icon='image', target_model='shelves.BannerShelf')), ('appshelf', shelves.blocks.AppShelfChooserBlock(icon='image', target_model='shelves.AppShelf')))),
        ),
    ]
